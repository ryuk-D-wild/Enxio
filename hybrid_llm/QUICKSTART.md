# Quick Start Guide

## Step 1: Install (First Time Only)

```bash
cd hybrid_llm
install.bat
```

This will:
- Create Python virtual environment
- Install PyTorch and dependencies
- Take ~5 minutes

## Step 2: Run the System

```bash
run.bat
```

First run will download the model (~6GB) - needs internet.

## Step 3: Use It

### Basic Commands:

```
>>> /code Write a REST API with FastAPI
>>> /web Search for async Python patterns
>>> /search python asyncio tutorial
>>> /offline (toggle offline mode)
>>> /quit
```

### Or just type directly:

```
>>> Create a function to parse JSON with error handling
```

## What You Need to Provide:

1. **Python 3.10+** - Check: `python --version`
2. **~10GB RAM** - For 7B model (or use 1.5B model for 4GB RAM)
3. **Internet** - First run only (downloads model)
4. **Codebase path** (optional) - Edit `config.json` to point to your projects

## Customization:

### Use Smaller Model (Less RAM):

Edit `config.json`:
```json
"model": {
  "name": "Qwen/Qwen2.5-Coder-1.5B-Instruct"
}
```

### Point to Your Codebase:

Edit `config.json`:
```json
"rag": {
  "codebase_path": "C:/Users/YourName/Projects"
}
```

### Verify Offline Mode:

```bash
python network_monitor.py
```

## Fine-Tuning (Optional):

1. Open `colab_training.ipynb` in Google Colab
2. Run all cells (uses free GPU)
3. Download the `qwen-finetuned.zip`
4. Extract to `hybrid_llm/models/`
5. Use `load_finetuned.py` to load it

## Troubleshooting:

**Out of Memory:**
- Use smaller model (1.5B instead of 7B)
- Close other programs
- Reduce `max_tokens` in config.json

**Model download fails:**
- Check internet connection
- Try again (Hugging Face can be slow)
- Use VPN if blocked in your region

**Network blocker errors:**
- This is GOOD - means model is offline
- Disable with `/offline` command if needed

## File Structure:

```
hybrid_llm/
├── install.bat          # Setup script
├── run.bat              # Start system
├── main.py              # Main entry point
├── config.json          # Configuration
├── rag_coder.py         # RAG + Code generation
├── web_search.py        # Internet search
├── network_monitor.py   # Offline verification
├── colab_training.ipynb # Fine-tuning notebook
└── load_finetuned.py    # Load trained model
```

## What to Expect:

✅ Can create novel code by combining patterns
✅ Learns from your codebase
✅ Can search web for docs
✅ Runs completely offline
✅ Fits in 50GB

❌ Won't match Sonnet accuracy (fundamental limitation)
❌ Struggles with very complex logic
❌ Limited context window (4K tokens)

## Next Steps:

1. Run `install.bat`
2. Run `run.bat`
3. Try: `/code Create a simple web scraper`
4. Point it to your codebase in config.json
5. Fine-tune on Colab with your own data
