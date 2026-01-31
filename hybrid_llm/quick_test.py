"""
Quick test - Load model and generate simple code
This will download the model on first run (~6GB)
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

print("=" * 70)
print("Quick Test - Loading Qwen Model")
print("=" * 70)
print("\nNOTE: First run will download ~6GB model")
print("This may take 10-30 minutes depending on your internet speed\n")

# Use smaller model for testing (1.5B instead of 7B)
MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"

print(f"Loading {MODEL_NAME}...")
print("Please wait...\n")

try:
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )
    print("✅ Tokenizer loaded")
    
    # Load model (CPU only, no quantization for first test)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float32,
        device_map="cpu",
        trust_remote_code=True,
        low_cpu_mem_usage=True,
    )
    print("✅ Model loaded")
    
    # Simple test
    print("\n" + "=" * 70)
    print("Testing code generation...")
    print("=" * 70)
    
    prompt = "Write a Python function to add two numbers"
    
    messages = [
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": prompt}
    ]
    
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    
    inputs = tokenizer(text, return_tensors="pt")
    
    print(f"\nPrompt: {prompt}")
    print("\nGenerating...")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.1,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )
    
    response = tokenizer.decode(
        outputs[0][inputs.input_ids.shape[1]:],
        skip_special_tokens=True
    )
    
    print("\n" + "-" * 70)
    print("Response:")
    print("-" * 70)
    print(response)
    print("-" * 70)
    
    print("\n✅ SUCCESS! Model is working!")
    print("\nNext steps:")
    print("1. Run 'run.bat' for full system with RAG and web search")
    print("2. Edit config.json to use 7B model for better quality")
    print("3. Point RAG to your codebase in config.json")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nTroubleshooting:")
    print("- Check internet connection (first run needs to download model)")
    print("- Make sure you have ~4GB free RAM")
    print("- Try closing other programs")
