# Model Management Guide

## 📍 Where Models Are Stored

All Qwen models are cached at:
```
C:\Users\Mi\.cache\huggingface\hub\
```

This is the **Hugging Face cache directory**. Models download here once and are reused by all scripts.

## 📦 Model Sizes

| Model | Size | RAM Needed | Speed (2-core) |
|-------|------|------------|----------------|
| Qwen 1.5B | ~3GB | 4GB | ~10-20s |
| Qwen 7B | ~7GB | 10GB | ~30-60s |

## ✅ Check What's Downloaded

Run this to see cached models:
```bash
python check_models.py
```

Output example:
```
✅ Complete
Model: Qwen/Qwen2.5-Coder-1.5B-Instruct
Size: 2.89 GB
Path: C:\Users\Mi\.cache\huggingface\hub\models--Qwen--Qwen2.5-Coder-1.5B-Instruct
```

## 📥 Download Models

### Option 1: During Installation (Recommended)

Models download automatically when you run:
```bash
# For 1.5B model
cd qwen_setup
install.bat

# For 7B model
cd hybrid_llm
install.bat
```

### Option 2: Manual Download

Use the download script:
```bash
download_models.bat
```

Choose:
1. Qwen 1.5B (~3GB) - For qwen_setup
2. Qwen 7B (~7GB) - For hybrid_llm  
3. Both models (~10GB total)

### Option 3: Python Command

```bash
# Download 1.5B
python -c "from huggingface_hub import snapshot_download; snapshot_download('Qwen/Qwen2.5-Coder-1.5B-Instruct')"

# Download 7B
python -c "from huggingface_hub import snapshot_download; snapshot_download('Qwen/Qwen2.5-Coder-7B-Instruct')"
```

## 🔄 How Caching Works

### First Time
```
run.bat
    ↓
Script tries to load model
    ↓
Model not in cache
    ↓
Downloads from Hugging Face (~3-7GB)
    ↓
Saves to cache
    ↓
Loads into RAM
    ↓
Ready to use
```

### Second Time (After Cache)
```
run.bat
    ↓
Script tries to load model
    ↓
Model found in cache ✅
    ↓
Loads directly from cache (fast!)
    ↓
Ready to use
```

## 🐛 Common Issues

### Issue: Scripts Get Stuck on "Downloading model..."

**Cause:** Model download interrupted or incomplete

**Solution:**
```bash
# 1. Check what's downloaded
python check_models.py

# 2. If incomplete, delete and re-download
# For 1.5B:
rmdir /s /q "%USERPROFILE%\.cache\huggingface\hub\models--Qwen--Qwen2.5-Coder-1.5B-Instruct"

# For 7B:
rmdir /s /q "%USERPROFILE%\.cache\huggingface\hub\models--Qwen--Qwen2.5-Coder-7B-Instruct"

# 3. Re-download
download_models.bat
```

### Issue: "Model downloading every time"

**Cause:** Scripts were trying to load before download complete

**Fixed:** Updated install.bat to download during installation, not during run

**Now:**
- `install.bat` downloads model
- `run.bat` loads from cache (fast)

### Issue: Out of disk space

**Solution:**
```bash
# Delete unused models
# Keep only what you need:

# If using qwen_setup only, delete 7B:
rmdir /s /q "%USERPROFILE%\.cache\huggingface\hub\models--Qwen--Qwen2.5-Coder-7B-Instruct"

# If using hybrid_llm only, delete 1.5B:
rmdir /s /q "%USERPROFILE%\.cache\huggingface\hub\models--Qwen--Qwen2.5-Coder-1.5B-Instruct"
```

## 📊 Current Status

Run `python check_models.py` to see:

**Expected after full setup:**
```
✅ Complete
Model: Qwen/Qwen2.5-Coder-1.5B-Instruct
Size: 2.89 GB

✅ Complete
Model: Qwen/Qwen2.5-Coder-7B-Instruct
Size: 6.85 GB

Total: ~10GB
```

## 🔧 Model Selection

### qwen_setup/ Uses:
- **Model:** Qwen/Qwen2.5-Coder-1.5B-Instruct
- **Why:** Faster, less RAM, good for testing
- **File:** `qwen_setup/qwen_coder.py` line 27

### hybrid_llm/ Uses:
- **Model:** Qwen/Qwen2.5-Coder-7B-Instruct  
- **Why:** Better quality, more accurate
- **File:** `hybrid_llm/config.json`

### Change Model:

**For qwen_setup:**
Edit `qwen_setup/qwen_coder.py`:
```python
# Line 27
MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"  # Change this
```

**For hybrid_llm:**
Edit `hybrid_llm/config.json`:
```json
{
  "model": {
    "name": "Qwen/Qwen2.5-Coder-7B-Instruct"  // Change this
  }
}
```

## 🗑️ Clean Up Cache

### Delete All Models
```bash
rmdir /s /q "%USERPROFILE%\.cache\huggingface\hub"
```

### Delete Specific Model
```bash
# 1.5B
rmdir /s /q "%USERPROFILE%\.cache\huggingface\hub\models--Qwen--Qwen2.5-Coder-1.5B-Instruct"

# 7B
rmdir /s /q "%USERPROFILE%\.cache\huggingface\hub\models--Qwen--Qwen2.5-Coder-7B-Instruct"
```

### Re-download After Cleanup
```bash
download_models.bat
```

## 📝 Summary

### What Changed (Fix)

**Before:**
- `run.bat` tried to load model
- If not cached, downloaded during run
- Scripts got stuck
- Downloaded every time

**After:**
- `install.bat` downloads model once
- `run.bat` loads from cache (fast)
- No more stuck scripts
- Download only once

### Files Updated

1. ✅ `qwen_setup/install.bat` - Now downloads 1.5B
2. ✅ `hybrid_llm/install.bat` - Now downloads 7B
3. ✅ `download_models.bat` - Manual download script
4. ✅ `check_models.py` - Check what's cached
5. ✅ `MODEL_MANAGEMENT.md` - This guide

### Quick Commands

```bash
# Check models
python check_models.py

# Download models
download_models.bat

# Clean cache
rmdir /s /q "%USERPROFILE%\.cache\huggingface\hub"

# Re-install
cd qwen_setup && install.bat
cd hybrid_llm && install.bat
```

---

**Last Updated:** January 19, 2026
**Status:** Fixed - Models now download during install, not run
