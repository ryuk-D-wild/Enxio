"""
Hybrid LLM System - Main Entry Point
Combines RAG, Web Search, and Offline Verification
"""

import json
import sys
from pathlib import Path
from rag_coder import RAGQwenCoder
from web_search import WebSearchTool
from network_monitor import offline_mode


class HybridLLM:
    """Complete hybrid system with all features."""
    
    def __init__(self, config_path: str = "config.json"):
        print("=" * 70)
        print("Hybrid LLM System - Initializing...")
        print("=" * 70)
        
        # Load config
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        # Initialize components
        print("\n[1/3] Loading RAG Coder...")
        self.coder = RAGQwenCoder(
            model_name=self.config['model']['name'],
            codebase_path=self.config['rag']['codebase_path']
        )
        
        print("\n[2/3] Initializing Web Search...")
        self.web_search = WebSearchTool()
        
        print("\n[3/3] Setting up network monitor...")
        self.offline_mode = self.config['network']['offline_mode']
        
        print("\n" + "=" * 70)
        print("✅ System Ready!")
        print("=" * 70)
    
    def generate_code(
        self,
        task: str,
        use_web: bool = False,
        use_rag: bool = True
    ) -> str:
        """
        Generate code with optional web search and RAG.
        
        Args:
            task: What to build
            use_web: Search internet for docs/examples
            use_rag: Use local codebase patterns
        """
        enhanced_task = task
        
        # Add web search context if requested
        if use_web:
            print("\n🌐 Searching web for relevant information...")
            search_results = self.web_search.search_duckduckgo(task, max_results=3)
            
            if search_results:
                enhanced_task += "\n\n## Web Search Results:\n"
                for i, result in enumerate(search_results, 1):
                    enhanced_task += f"\n{i}. {result['title']}\n"
                    enhanced_task += f"   {result['snippet']}\n"
        
        # Generate with RAG
        print("\n🧠 Generating code...")
        result = self.coder.generate_novel_code(
            enhanced_task,
            use_rag=use_rag,
            temperature=self.config['generation']['temperature']
        )
        
        return result
    
    def interactive_mode(self):
        """Interactive coding assistant."""
        print("\n" + "=" * 70)
        print("Commands:")
        print("  /code <task>       - Generate code (RAG only)")
        print("  /web <task>        - Generate with web search")
        print("  /search <query>    - Search web only")
        print("  /offline           - Toggle offline mode")
        print("  /config            - Show current config")
        print("  /quit              - Exit")
        print("=" * 70)
        
        while True:
            try:
                print("\n" + "-" * 70)
                user_input = input(">>> ").strip()
                
                if not user_input:
                    continue
                
                if user_input == "/quit":
                    print("Goodbye!")
                    break
                
                elif user_input == "/config":
                    print(json.dumps(self.config, indent=2))
                
                elif user_input == "/offline":
                    self.offline_mode = not self.offline_mode
                    status = "ON" if self.offline_mode else "OFF"
                    print(f"Offline mode: {status}")
                
                elif user_input.startswith("/search "):
                    query = user_input[8:]
                    results = self.web_search.search_duckduckgo(query)
                    for i, r in enumerate(results, 1):
                        print(f"\n{i}. {r['title']}")
                        print(f"   {r['url']}")
                        print(f"   {r['snippet']}")
                
                elif user_input.startswith("/code "):
                    task = user_input[6:]
                    result = self.generate_code(task, use_web=False, use_rag=True)
                    print("\n" + "=" * 70)
                    print(result)
                    print("=" * 70)
                
                elif user_input.startswith("/web "):
                    task = user_input[5:]
                    result = self.generate_code(task, use_web=True, use_rag=True)
                    print("\n" + "=" * 70)
                    print(result)
                    print("=" * 70)
                
                else:
                    # Default: treat as code generation task
                    result = self.generate_code(user_input, use_web=False, use_rag=True)
                    print("\n" + "=" * 70)
                    print(result)
                    print("=" * 70)
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")


def main():
    """Main entry point."""
    
    # Check if config exists
    if not Path("config.json").exists():
        print("ERROR: config.json not found!")
        print("Please run from the hybrid_llm directory")
        sys.exit(1)
    
    # Initialize system
    system = HybridLLM()
    
    # Start interactive mode
    system.interactive_mode()


if __name__ == "__main__":
    main()
