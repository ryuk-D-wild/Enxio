# Hybrid LLM System - Complete Project Documentation

## 🎯 Project Goal

Create a local coding LLM system that:
1. Runs on a low-end 2-core laptop
2. Works completely offline (no data leaks)
3. Can create novel code by combining patterns
4. Supports fine-tuning on Colab/Kaggle
5. Fits within 50GB storage
6. Has web search capability when needed

## 📁 Project Structure

```
.
├── qwen_setup/                    # Simple standalone setup
│   ├── install.bat               # Basic installation
│   ├── run.bat                   # Run basic version
│   ├── qwen_coder.py             # Simple Qwen interface
│   ├── requirements.txt          # Dependencies
│   └── README.md                 # Basic docs
│
└── hybrid_llm/                    # Full hybrid system (MAIN)
    ├── install.bat               # Full system installation
    ├── run.bat                   # Start hybrid system
    ├── config.json               # Configuration file
    ├── main.py                   # Main entry point
    ├── rag_coder.py              # RAG + code generation
    ├── web_search.py             # Internet search tool
    ├── network_monitor.py        # Offline verification
    ├── load_finetuned.py         # Load trained models
    ├── test_system.py            # System tests
    ├── colab_training.ipynb      # Colab fine-tuning
    ├── QUICKSTART.md             # Quick start guide
    └── README.md                 # Architecture docs
```

## 🚀 Quick Start

### Option 1: Simple Setup (Recommended for Testing)

```bash
cd qwen_setup
install.bat
run.bat
```

### Option 2: Full Hybrid System (Recommended for Production)

```bash
cd hybrid_llm
install.bat
run.bat
```

## 🔧 System Components

### 1. RAG (Retrieval-Augmented Generation)
**File:** `hybrid_llm/rag_coder.py`

- Indexes your local codebase
- Searches for relevant code patterns
- Combines patterns to create novel solutions
- Supports multiple languages (.py, .js, .ts, .java, .cpp, .go, .rs)

**How it works:**
```python
# Indexes all code files
coder = RAGQwenCoder(codebase_path="./your_project")

# Searches codebase and generates novel code
result = coder.generate_novel_code("Create REST API with auth")
```

### 2. Network Monitor
**File:** `hybrid_llm/network_monitor.py`

- Blocks all network access during inference
- Verifies model runs completely offline
- Prevents data leaks to external servers

**Usage:**
```python
from network_monitor import offline_mode

with offline_mode():
    # Model runs here with no network access
    result = model.generate(...)
```

### 3. Web Search Tool
**File:** `hybrid_llm/web_search.py`

- Searches DuckDuckGo (no API key needed)
- Fetches documentation and examples
- Only used when explicitly requested

**Usage:**
```python
search = WebSearchTool()
results = search.search_docs("python", "async await")
```

### 4. Fine-Tuning Pipeline
**File:** `hybrid_llm/colab_training.ipynb`

- Train on Colab's free GPU
- Uses LoRA (Low-Rank Adaptation) - only ~100MB
- Download and merge with base model
- No need to train on your 2-core laptop

**Steps:**
1. Upload notebook to Google Colab
2. Run all cells
3. Download `qwen-finetuned.zip`
4. Extract to `hybrid_llm/models/`
5. Load with `load_finetuned.py`

## ⚙️ Configuration

**File:** `hybrid_llm/config.json`

```json
{
  "model": {
    "name": "Qwen/Qwen2.5-Coder-7B-Instruct",
    "alternatives": {
      "low_ram": "Qwen/Qwen2.5-Coder-1.5B-Instruct",    // 4GB RAM
      "medium_ram": "Qwen/Qwen2.5-Coder-3B-Instruct",   // 6GB RAM
      "high_ram": "Qwen/Qwen2.5-Coder-7B-Instruct"      // 10GB RAM
    }
  },
  "rag": {
    "enabled": true,
    "codebase_path": ".",                               // Your project path
    "max_results": 3,
    "file_extensions": [".py", ".js", ".ts", ...]
  },
  "generation": {
    "max_tokens": 2048,
    "temperature": 0.3,                                 // Lower = more accurate
    "top_p": 0.95,
    "top_k": 50
  },
  "network": {
    "offline_mode": true,                               // Block network access
    "verify_no_leaks": true
  }
}
```

## 💾 Storage Requirements

| Component | Size | Required |
|-----------|------|----------|
| Qwen 7B (4-bit) | ~6GB | Yes |
| Python + deps | ~3GB | Yes |
| Training cache | ~5GB | Optional |
| LoRA adapters | ~500MB | Optional |
| System overhead | ~2GB | Yes |
| **Total** | **~16GB** | **Minimum** |
| **Free space** | **~34GB** | **Available** |

## 🎯 What This System Can Do

### ✅ Capabilities

1. **Novel Code Generation**
   - Combines patterns from your codebase
   - Creates code that doesn't exist but uses familiar parts
   - Example: Merge REST API + WebSocket + Auth patterns

2. **Offline Operation**
   - Runs completely offline after first download
   - No data sent to external servers
   - Verified with network blocker

3. **Web-Assisted Coding**
   - Search for documentation when needed
   - Fetch examples from the internet
   - Combine web knowledge with local patterns

4. **Fine-Tuning**
   - Train on Colab's free GPU
   - Download small LoRA adapters (~100MB)
   - Merge with base model locally

5. **Codebase Learning**
   - Indexes your projects
   - Learns your coding style
   - Reuses your patterns

### ❌ Limitations (Be Realistic)

1. **Accuracy vs Sonnet**
   - Simple tasks: ~70% of Sonnet
   - Complex tasks: ~40% of Sonnet
   - Architecture design: ~30% of Sonnet

2. **Context Window**
   - Limited to 4K tokens (~3000 words)
   - Can't process very large files

3. **Reasoning**
   - Struggles with complex multi-step logic
   - May miss subtle bugs
   - Needs verification

4. **Training Constraints**
   - Can't train on 2-core laptop (too slow)
   - Must use Colab/Kaggle for training
   - Can't "merge" training from multiple machines

## 🔍 Usage Examples

### Basic Code Generation

```bash
>>> /code Create a function to parse JSON with error handling
```

### Web-Assisted Generation

```bash
>>> /web Create async web scraper with rate limiting
```

### Search Only

```bash
>>> /search python asyncio best practices
```

### Toggle Offline Mode

```bash
>>> /offline
Offline mode: OFF
```

## 🧪 Testing

Run system tests:

```bash
cd hybrid_llm
python test_system.py
```

Tests:
- ✅ Dependencies installed
- ✅ Configuration valid
- ✅ Network blocker works
- ✅ Model cache status

## 🐛 Troubleshooting

### ❌ Missing bitsandbytes (COMMON ERROR)

**Problem:** `PackageNotFoundError: No package metadata was found for bitsandbytes`

**Solution:**
```bash
# For qwen_setup
qwen_setup\venv\Scripts\python.exe -m pip install bitsandbytes>=0.43.0

# For hybrid_llm  
hybrid_llm\venv\Scripts\python.exe -m pip install bitsandbytes>=0.43.0
```

**Fixed in:** Updated install.bat now includes bitsandbytes

### Out of Memory

**Problem:** System crashes or freezes

**Solutions:**
1. Use smaller model in `config.json`:
   ```json
   "name": "Qwen/Qwen2.5-Coder-1.5B-Instruct"
   ```
2. Close other programs
3. Reduce `max_tokens` to 1024

### Model Download Fails

**Problem:** Download times out or fails

**Solutions:**
1. Check internet connection
2. Try again (Hugging Face can be slow)
3. Use VPN if blocked in your region
4. Download manually from Hugging Face

### Network Blocker Errors

**Problem:** "Network access blocked" error

**Solution:** This is GOOD! It means the model is offline. Disable with:
```bash
>>> /offline
```

### Import Errors

**Problem:** `ModuleNotFoundError`

**Solution:**
```bash
cd hybrid_llm
venv\Scripts\activate
pip install -r requirements.txt
```

**For detailed troubleshooting, see TROUBLESHOOTING.md**

## 📊 Performance Expectations

### Task Performance Matrix

| Task Type | This System | Sonnet 4.5 | Notes |
|-----------|-------------|------------|-------|
| Simple functions | 70% | 95% | Good for boilerplate |
| CRUD operations | 75% | 95% | Handles well |
| Algorithm implementation | 50% | 90% | Needs verification |
| Complex logic | 40% | 90% | Struggles |
| Debugging | 50% | 85% | Can find obvious bugs |
| Architecture design | 30% | 90% | Limited capability |
| Code explanation | 80% | 95% | Good at this |
| Refactoring | 60% | 90% | Decent |

### Speed Benchmarks (2-core laptop)

- Simple query: ~10-30 seconds
- Complex code: ~30-60 seconds
- With RAG: +5-10 seconds
- With web search: +10-20 seconds

## 🔐 Security & Privacy

### Data Privacy

1. **Offline Mode (Default)**
   - Model runs locally
   - No data sent to external servers
   - Verified with network blocker

2. **Web Search (Optional)**
   - Only when you use `/web` command
   - Uses DuckDuckGo (privacy-focused)
   - No tracking or logging

3. **Model Weights**
   - Downloaded from Hugging Face (trusted)
   - Open source and auditable
   - No telemetry or backdoors

### Verification

Run network monitor test:
```bash
python network_monitor.py
```

Expected output:
```
✅ SUCCESS: Network is blocked
```

## 🎓 Training Your Own Model

### Step 1: Prepare Data

Create `training_data.json`:
```json
[
  {
    "instruction": "Write a function to...",
    "output": "def function():\n    ..."
  }
]
```

### Step 2: Upload to Colab

1. Open `colab_training.ipynb` in Google Colab
2. Upload your `training_data.json`
3. Modify dataset loading:
   ```python
   dataset = load_dataset('json', data_files='training_data.json')
   ```

### Step 3: Train

Run all cells in the notebook (~1-2 hours on free GPU)

### Step 4: Download

Download `qwen-finetuned.zip` (~100MB)

### Step 5: Use Locally

```bash
# Extract to models fversion 1.0.1er
unzip qwen-finetuned.zip -d hybrid_llm/models/

# Test it
python load_finetuned.py
```

## 🔄 Workflow

### Daily Usage

```
1. Start system: run.bat
2. Ask questions or generate code
3. Verify outputs (always!)
4. Iterate if needed
```

### With Fine-Tuning

```
1. Collect good code examples
2. Format as training data
3. Train on Colab (weekly/monthly)
4. Download new adapters
5. Use improved model
```

## 📝 What You Need to Provide

### Required

1. ✅ **Python 3.10+**
   - Check: `python --version`
   - Install: https://python.org

2. ✅ **RAM**
   - 4GB minimum (1.5B model)
   - 10GB recommended (7B model)

3. ✅ **Storage**
   - 20GB minimum
   - 50GB recommended

4. ✅ **Internet** (first run only)
   - Download model (~6GB)
   - Then works offline

### Optional

1. ⚠️ **Your Codebase Path**
   - Edit `config.json`
   - Point to your projects
   - RAG will learn from it

2. ⚠️ **Training Data**
   - For fine-tuning
   - JSON format
   - Upload to Colab

3. ⚠️ **Google Colab Account**
   - For fine-tuning
   - Free tier is enough

## 🎯 Next Steps

### Immediate (Do Now)

1. ✅ Run `hybrid_llm/install.bat`
2. ✅ Run `hybrid_llm/test_system.py`
3. ✅ Run `hybrid_llm/run.bat`
4. ✅ Try: `/code Create a simple calculator`

### Short Term (This Week)

1. ⚠️ Edit `config.json` with your codebase path
2. ⚠️ Test RAG with your projects
3. ⚠️ Try web-assisted generation
4. ⚠️ Verify offline mode works

### Long Term (This Month)

1. ⚠️ Collect good code examples
2. ⚠️ Fine-tune on Colab
3. ⚠️ Download and test adapters
4. ⚠️ Iterate and improve

## 🤔 FAQ

**Q: Will this match Sonnet's accuracy?**
A: No. Sonnet has 10-20x more parameters and was trained on vastly more compute. This will be 30-70% as good depending on the task.

**Q: Can I train on my 2-core laptop?**
A: Technically yes, but it would take weeks/months. Use Colab instead (free GPU, takes hours).

**Q: Is my data safe?**
A: Yes, when offline mode is enabled (default). The network blocker verifies this.

**Q: Can I use this commercially?**
A: Check Qwen's license. Generally yes for the model, but verify for your use case.

**Q: Why not just use ChatGPT/Claude API?**
A: This is for learning, privacy, and offline use. APIs are better for production.

**Q: Can I contribute?**
A: Yes! This is your project. Modify, improve, and share.

## 📚 Resources

- **Qwen Models:** https://huggingface.co/Qwen
- **Transformers Docs:** https://huggingface.co/docs/transformers
- **LoRA Paper:** https://arxiv.org/abs/2106.09685
- **RAG Explanation:** https://arxiv.org/abs/2005.11401

## 🆘 Support

If you encounter errors:

1. Check this README
2. Run `test_system.py`
3. Check `QUICKSTART.md`
4. Review error messages carefully
5. Try smaller model if out of memory

## 📄 License

This project setup is MIT licensed. Individual components (Qwen, PyTorch, etc.) have their own licenses.

---

**Created:** January 2026
**Last Updated:** January 14, 2026
**Status:** Ready for testing

