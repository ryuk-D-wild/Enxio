"""
Check which Qwen models are cached
"""

import os
from pathlib import Path

cache_dir = Path.home() / '.cache' / 'huggingface' / 'hub'

print("=" * 70)
print("Cached Qwen Models")
print("=" * 70)
print(f"\nCache location: {cache_dir}")
print()

if not cache_dir.exists():
    print("❌ Cache directory doesn't exist")
    print("No models downloaded yet")
else:
    models = list(cache_dir.glob('models--Qwen*'))
    
    if not models:
        print("❌ No Qwen models found")
        print("Run download_models.bat to download")
    else:
        print("✅ Found models:")
        print()
        
        for model_dir in models:
            model_name = model_dir.name.replace('models--', '').replace('--', '/')
            
            # Calculate size
            total_size = sum(f.stat().st_size for f in model_dir.rglob('*') if f.is_file())
            size_gb = total_size / (1024**3)
            
            # Check if complete (has model.safetensors or pytorch_model.bin)
            has_weights = any(model_dir.rglob('model.safetensors')) or any(model_dir.rglob('pytorch_model.bin'))
            status = "✅ Complete" if has_weights and size_gb > 1 else "⚠️ Incomplete"
            
            print(f"  {status}")
            print(f"  Model: {model_name}")
            print(f"  Size: {size_gb:.2f} GB")
            print(f"  Path: {model_dir}")
            print()

print("=" * 70)
print("\nUsage:")
print("  - qwen_setup uses: Qwen/Qwen2.5-Coder-1.5B-Instruct")
print("  - hybrid_llm uses: Qwen/Qwen2.5-Coder-7B-Instruct")
print()
print("To download missing models:")
print("  python download_models.bat")
print("=" * 70)
