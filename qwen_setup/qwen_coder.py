"""
Qwen2.5-Coder Local Setup - Optimized for Low-End Hardware
Maximizes accuracy through careful prompting and inference settings
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import warnings
warnings.filterwarnings("ignore")


class QwenCoder:
    def __init__(self, model_name="Qwen/Qwen2.5-Coder-1.5B-Instruct"):
        """
        Initialize Qwen Coder with 4-bit quantization for low RAM usage.
        
        Model options (pick based on your RAM):
        - Qwen/Qwen2.5-Coder-0.5B-Instruct  (~1GB RAM)
        - Qwen/Qwen2.5-Coder-1.5B-Instruct  (~2GB RAM) [DEFAULT]
        - Qwen/Qwen2.5-Coder-3B-Instruct    (~4GB RAM)
        - Qwen/Qwen2.5-Coder-7B-Instruct    (~6GB RAM with 4-bit)
        """
        print(f"Loading {model_name}...")
        print("This may take a few minutes on first run (downloading model)...")
        
        # 4-bit quantization config - crucial for low-end hardware
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,  # Extra compression
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
        print("Model loaded successfully!")
    
    def generate(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.1,  # Low temp = more accurate/deterministic
        top_p: float = 0.95,
        top_k: int = 50,
        repetition_penalty: float = 1.1,
    ) -> str:
        """
        Generate code with optimized settings for accuracy.
        
        Lower temperature (0.1-0.3) = more accurate, less creative
        Higher temperature (0.7-1.0) = more creative, less predictable
        """
        messages = [
            {
                "role": "system",
                "content": self._get_system_prompt()
            },
            {
                "role": "user", 
                "content": prompt
            }
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
                max_new_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                repetition_penalty=repetition_penalty,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
            )
        
        response = self.tokenizer.decode(
            outputs[0][inputs.input_ids.shape[1]:],
            skip_special_tokens=True
        )
        
        return response.strip()
    
    def _get_system_prompt(self) -> str:
        """
        Carefully crafted system prompt to maximize coding accuracy.
        This is where we can actually improve output quality.
        """
        return """You are an expert software engineer. Follow these rules strictly:

1. ACCURACY: Write correct, bug-free code. Double-check logic before responding.
2. COMPLETE: Provide full implementations, not snippets or pseudocode.
3. BEST PRACTICES: Use proper error handling, type hints, and documentation.
4. EXPLAIN: Briefly explain your approach before the code.
5. TEST: Include example usage or test cases when relevant.

Think step-by-step before coding. If unsure, state assumptions clearly."""

    def code(self, task: str) -> str:
        """Shorthand for coding tasks with optimal settings."""
        return self.generate(task, temperature=0.1)
    
    def explain(self, code: str) -> str:
        """Explain existing code."""
        prompt = f"Explain this code in detail:\n\n```\n{code}\n```"
        return self.generate(prompt, temperature=0.3)
    
    def debug(self, code: str, error: str = "") -> str:
        """Debug code with optional error message."""
        prompt = f"Debug this code and fix any issues:\n\n```\n{code}\n```"
        if error:
            prompt += f"\n\nError message: {error}"
        return self.generate(prompt, temperature=0.1)
    
    def refactor(self, code: str) -> str:
        """Refactor code for better quality."""
        prompt = f"Refactor this code to improve readability, performance, and best practices:\n\n```\n{code}\n```"
        return self.generate(prompt, temperature=0.2)


def main():
    """Interactive coding assistant."""
    print("=" * 60)
    print("Qwen Coder - Local Coding Assistant")
    print("=" * 60)
    print("\nCommands:")
    print("  /code <task>    - Write code for a task")
    print("  /debug <code>   - Debug code")
    print("  /explain <code> - Explain code")
    print("  /quit           - Exit")
    print("  Or just type your question directly")
    print("=" * 60)
    
    # Initialize - use smaller model if you have <4GB RAM
    coder = QwenCoder("Qwen/Qwen2.5-Coder-1.5B-Instruct")
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "/quit":
                print("Goodbye!")
                break
            
            if user_input.startswith("/code "):
                task = user_input[6:]
                print("\nGenerating code...\n")
                response = coder.code(task)
            elif user_input.startswith("/debug "):
                code = user_input[7:]
                print("\nDebugging...\n")
                response = coder.debug(code)
            elif user_input.startswith("/explain "):
                code = user_input[9:]
                print("\nExplaining...\n")
                response = coder.explain(code)
            else:
                print("\nThinking...\n")
                response = coder.generate(user_input)
            
            print(response)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
