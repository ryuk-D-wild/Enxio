"""
RAG-Enhanced Qwen Coder
Can reference local code/docs to create novel combinations
"""

import os
import json
from pathlib import Path
from typing import List, Dict
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


class CodebaseRAG:
    """Simple RAG system for local code reference."""
    
    def __init__(self, codebase_path: str = "."):
        self.codebase_path = Path(codebase_path)
        self.code_index = {}
        self._index_codebase()
    
    def _index_codebase(self):
        """Index all code files for quick retrieval."""
        extensions = {'.py', '.js', '.ts', '.java', '.cpp', '.c', '.go', '.rs'}
        
        for ext in extensions:
            for file_path in self.codebase_path.rglob(f'*{ext}'):
                if 'venv' in str(file_path) or 'node_modules' in str(file_path):
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        self.code_index[str(file_path)] = {
                            'content': content,
                            'language': ext[1:],
                            'size': len(content)
                        }
                except:
                    pass
        
        print(f"Indexed {len(self.code_index)} code files")
    
    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Simple keyword-based search (can be upgraded to embeddings)."""
        results = []
        query_lower = query.lower()
        
        for path, data in self.code_index.items():
            content_lower = data['content'].lower()
            
            # Count keyword matches
            score = sum(content_lower.count(word) for word in query_lower.split())
            
            if score > 0:
                results.append({
                    'path': path,
                    'score': score,
                    'content': data['content'][:1000],  # First 1000 chars
                    'language': data['language']
                })
        
        # Sort by score and return top_k
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]


class RAGQwenCoder:
    """Qwen Coder with RAG for novel code generation."""
    
    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-Coder-7B-Instruct",
        codebase_path: str = "."
    ):
        print("Initializing RAG-Enhanced Qwen Coder...")
        
        # Initialize RAG
        self.rag = CodebaseRAG(codebase_path)
        
        # Load model with 4-bit quantization
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
        
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            trust_remote_code=True
        )
        
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            quantization_config=quantization_config,
            device_map="auto",
            trust_remote_code=True,
            low_cpu_mem_usage=True,
        )
        
        self.model.eval()
        print("Ready!")
    
    def generate_novel_code(
        self,
        task: str,
        use_rag: bool = True,
        temperature: float = 0.3  # Higher for creativity
    ) -> str:
        """
        Generate novel code by combining patterns from codebase.
        
        Args:
            task: What to build
            use_rag: Whether to search codebase for reference
            temperature: Higher = more creative combinations
        """
        context = ""
        
        if use_rag:
            # Search for relevant code patterns
            results = self.rag.search(task, top_k=3)
            
            if results:
                context = "\n\n## Reference Code Patterns:\n"
                for i, result in enumerate(results, 1):
                    context += f"\n### Pattern {i} ({result['language']}):\n"
                    context += f"```{result['language']}\n{result['content']}\n```\n"
        
        # Build prompt
        system_prompt = """You are an expert at creating novel code by combining existing patterns.

Your approach:
1. Analyze the reference patterns (if provided)
2. Identify reusable concepts and techniques
3. Combine them in NEW ways to solve the task
4. Create code that doesn't exist but uses familiar parts

Be creative but practical. The code must work."""

        user_prompt = f"""Task: {task}
{context}

Create novel code that solves this task by combining and adapting the patterns above.
Think step-by-step about how to merge these concepts."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=2048,
                temperature=temperature,
                top_p=0.95,
                top_k=50,
                repetition_penalty=1.1,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
            )
        
        response = self.tokenizer.decode(
            outputs[0][inputs.input_ids.shape[1]:],
            skip_special_tokens=True
        )
        
        return response.strip()


def main():
    """Demo: Create novel code from existing patterns."""
    
    print("=" * 70)
    print("RAG-Enhanced Qwen Coder - Novel Code Generation")
    print("=" * 70)
    print("\nThis system can create NEW code by combining patterns from your codebase")
    print("\nExamples:")
    print("  'Create a REST API with WebSocket fallback'")
    print("  'Build a caching layer using Redis and local storage'")
    print("  'Make an async task queue with retry logic'")
    print("=" * 70)
    
    # Initialize (point to your codebase)
    coder = RAGQwenCoder(
        model_name="Qwen/Qwen2.5-Coder-7B-Instruct",
        codebase_path="."  # Change to your project path
    )
    
    while True:
        try:
            print("\n" + "=" * 70)
            task = input("What novel code should I create? (or 'quit'): ").strip()
            
            if task.lower() == 'quit':
                break
            
            if not task:
                continue
            
            print("\n🔍 Searching codebase for relevant patterns...")
            print("🧠 Combining concepts to create novel solution...")
            print("\n" + "-" * 70)
            
            result = coder.generate_novel_code(task, use_rag=True, temperature=0.4)
            
            print(result)
            print("-" * 70)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
    
    print("\nGoodbye!")


if __name__ == "__main__":
    main()
