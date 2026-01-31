"""
Load fine-tuned LoRA adapters from Colab training
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel


def load_finetuned_model(
    base_model: str = "Qwen/Qwen2.5-Coder-7B-Instruct",
    adapter_path: str = "./models/qwen-finetuned"
):
    """
    Load base model + fine-tuned LoRA adapters.
    
    Args:
        base_model: Original Qwen model name
        adapter_path: Path to downloaded LoRA adapters from Colab
    """
    print("Loading fine-tuned model...")
    
    # Load base model with quantization
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )
    
    base = AutoModelForCausalLM.from_pretrained(
        base_model,
        quantization_config=quantization_config,
        device_map="auto",
        trust_remote_code=True,
    )
    
    # Load LoRA adapters
    model = PeftModel.from_pretrained(base, adapter_path)
    
    tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
    
    print("Fine-tuned model loaded!")
    return model, tokenizer


def test_finetuned():
    """Test the fine-tuned model."""
    model, tokenizer = load_finetuned_model()
    
    test_prompt = "Write a Python function to reverse a string"
    
    inputs = tokenizer(test_prompt, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.1,
            do_sample=True
        )
    
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("\nTest Result:")
    print("=" * 70)
    print(result)
    print("=" * 70)


if __name__ == "__main__":
    test_finetuned()
