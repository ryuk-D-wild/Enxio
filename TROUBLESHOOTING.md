# Troubleshooting Guide

## Common Errors and Solutions

### ❌ Error: `PackageNotFoundError: No package metadata was found for bitsandbytes`

**Problem:** Missing bitsandbytes package (needed for 4-bit quantization)

**Solution:**
```bash
# For qwen_setup
qwen_setup\venv\Scripts\python.exe -m pip install bitsandbytes>=0.43.0

# For hybrid_llm
hybrid_llm\venv\Scripts\python.exe -m pip install bitsandbytes>=0.43.0
```

**Prevention:** Run the install.bat script which now includes bitsandbytes

---

### ❌ Error: Out of Memory / System Freeze

**Problem:** Model too large for your RAM

**Solutions:**

1. **Use smaller model** - Edit the Python file:
   ```python
   # Change from 7B to 1.5B
   MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
   ```

2. **Close other programs** - Free up RAM

3. **Disable quantization** (uses more RAM but might work):
   ```python
   # Remove quantization_config parameter
   model = AutoModelForCausalLM.from_pretrained(
       MODEL_NAME,
       device_map="cpu",
       trust_remote_code=True,
   )
   ```

**RAM Requirements:**
- 0.5B model: ~2GB RAM
- 1.5B model: ~4GB RAM  
- 3B model: ~6GB RAM
- 7B model: ~10GB RAM

---

### ❌ Error: Model Download Fails / Timeout

**Problem:** Slow or interrupted download from Hugging Face

**Solutions:**

1. **Retry** - Downloads resume automatically
2. **Check internet** - Stable connection needed
3. **Use VPN** - If Hugging Face is blocked
4. **Manual download:**
   ```bash
   # Download manually from https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct
   # Place in: C:\Users\YourName\.cache\huggingface\hub\
   ```

---

### ❌ Error: `ImportError: cannot import name 'AutoModelForCausalLM'`

**Problem:** Transformers not installed or wrong version

**Solution:**
```bash
pip install transformers>=4.37.0 --upgrade
```

---

### ❌ Error: Network Access Blocked (in offline mode)

**Problem:** This is actually GOOD - means offline mode is working!

**Solution:** If you need internet access:
```bash
# In the interactive prompt
>>> /offline
```

Or disable in config.json:
```json
"network": {
  "offline_mode": false
}
```

---

### ❌ Error: Slow Generation (30+ seconds per response)

**Problem:** Normal on 2-core CPU, but can be improved

**Solutions:**

1. **Use smaller model** (1.5B instead of 7B)
2. **Reduce max_tokens** in config.json:
   ```json
   "generation": {
     "max_tokens": 512
   }
   ```
3. **Close background programs**
4. **Consider using GPU** (if available)

---

### ❌ Error: `ModuleNotFoundError: No module named 'torch'`

**Problem:** Virtual environment not activated

**Solution:**
```bash
# Activate venv first
cd qwen_setup  # or hybrid_llm
venv\Scripts\activate
python qwen_coder.py
```

Or use the batch files:
```bash
run.bat
```

---

### ❌ Error: Code Quality is Poor

**Problem:** Model limitations or wrong settings

**Solutions:**

1. **Use larger model** (7B instead of 1.5B)
2. **Lower temperature** for more accurate code:
   ```json
   "generation": {
     "temperature": 0.1
   }
   ```
3. **Better prompts** - Be specific:
   - ❌ "make a function"
   - ✅ "Write a Python function that takes a list of integers and returns the sum, with error handling for empty lists"

4. **Use RAG** - Point to your codebase in config.json
5. **Fine-tune** - Train on your own code examples

---

### ❌ Error: RAG Not Finding Code

**Problem:** Codebase path wrong or no code indexed

**Solutions:**

1. **Check path** in config.json:
   ```json
   "rag": {
     "codebase_path": "C:/Users/YourName/Projects"
   }
   ```

2. **Verify files exist:**
   ```bash
   python
   >>> from rag_coder import CodebaseRAG
   >>> rag = CodebaseRAG(".")
   >>> print(len(rag.code_index))  # Should be > 0
   ```

3. **Check file extensions** - Only indexes: .py, .js, .ts, .java, .cpp, .go, .rs

---

### ❌ Error: Web Search Not Working

**Problem:** Network issues or DuckDuckGo blocking

**Solutions:**

1. **Check internet connection**
2. **Try different search:**
   ```bash
   >>> /search python tutorial
   ```
3. **Disable if not needed** - Use `/code` instead of `/web`

---

### ❌ Error: Fine-tuned Model Won't Load

**Problem:** LoRA adapters not found or incompatible

**Solutions:**

1. **Check path:**
   ```python
   adapter_path = "./models/qwen-finetuned"  # Must exist
   ```

2. **Verify files:**
   ```
   models/qwen-finetuned/
   ├── adapter_config.json
   ├── adapter_model.bin
   └── ...
   ```

3. **Re-download from Colab** if corrupted

---

## Installation Issues

### Python Not Found

**Solution:**
1. Install Python 3.10+ from https://python.org
2. Check "Add to PATH" during installation
3. Restart terminal

### Pip Install Fails

**Solution:**
```bash
python -m pip install --upgrade pip
python -m pip install <package> --no-cache-dir
```

### Virtual Environment Issues

**Solution:**
```bash
# Delete and recreate
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Performance Optimization

### Speed Up Generation

1. Use smaller model
2. Reduce max_tokens
3. Disable RAG if not needed
4. Use temperature=0.1 (faster, more deterministic)

### Reduce Memory Usage

1. Use 4-bit quantization (default)
2. Close other programs
3. Use smaller model
4. Reduce context window

### Improve Quality

1. Use larger model (7B)
2. Lower temperature (0.1-0.2)
3. Better prompts
4. Fine-tune on your data
5. Use RAG with good codebase

---

## Getting Help

1. **Check this guide first**
2. **Read PROJECT_OVERVIEW.md** for architecture
3. **Run test_system.py** to diagnose:
   ```bash
   cd hybrid_llm
   .\venv\Scripts\python.exe test_system.py
   ```
4. **Check error messages** - They usually tell you what's wrong
5. **Try smaller model** - Often solves memory issues

---

## Quick Fixes Checklist

- [ ] Virtual environment activated?
- [ ] All dependencies installed? (`pip list`)
- [ ] Enough RAM? (Check Task Manager)
- [ ] Internet working? (First run only)
- [ ] Using correct model name?
- [ ] Config.json exists and valid?
- [ ] Paths in config.json correct?
- [ ] Tried smaller model?
- [ ] Closed other programs?
- [ ] Restarted terminal?

---

**Last Updated:** January 18, 2026
**Status:** Active troubleshooting guide
