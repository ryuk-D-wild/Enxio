"""
Pre-download Qwen models to cache
Run this once to download both models
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
import os

print("=" * 70)
print("Qwen Model Downloader")
print("=" * 70)
print("\nThis will download models to:")
print(f"{os.path.expanduser('~')}/.cache/huggingface/hub/")
print("\nModels will be cached and reused by both systems")
print("=" * 70)

models = [
    ("Qwen/Qwen2.5-Coder-1.5B-Instruct", "1.5B", "~3GB"),
    ("Qwen/Qwen2.5-Coder-7B-Instruct", "7B", "~7GB"),
]

for model_name, size, disk_size in models:
    print(f"\n{'=' * 70}")
    print(f"Downloading {size} model ({disk_size})...")
    print(f"Model: {model_name}")
    print("=" * 70)
    
    try:
        # Download tokenizer
        print("\n[1/2] Downloading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            trust_remote_code=True
        )
        print("✅ Tokenizer downloaded")
        
        # Download model (just download, don't load into RAM)
        print("\n[2/2] Downloading model weights...")
        print("(This may take 10-30 minutes depending on internet speed)")
        
        # Use snapshot_download to just download without loading
        from huggingface_hub import snapshot_download
        snapshot_download(
            repo_id=model_name,
            cache_dir=os.path.expanduser("~/.cache/huggingface/hub"),
            ignore_patterns=["*.msgpack", "*.h5", "*.ot"]  # Skip unnecessary files
        )
        
        print(f"✅ {size} model downloaded successfully!")
        
    except Exception as e:
        print(f"❌ Error downloading {size} model: {e}")
        print("You can try again later or skip this model")

print("\n" + "=" * 70)
print("Download Complete!")
print("=" * 70)
print("\nModels are cached at:")
print(f"{os.path.expanduser('~')}/.cache/huggingface/hub/")
print("\nYou can now run:")
print("  - qwen_setup/run.bat (uses 1.5B)")
print("  - hybrid_llm/run.bat (uses 7B)")
print("\nThey will load from cache instantly!")
print("=" * 70)
