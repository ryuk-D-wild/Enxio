# Lambda Driver - Archive

## ⚠️ This is version 1.0.1 
**Status:** Archived for reference only  
**Date Archived:** January 19, 2026  
**Replaced By:** v2.0.0  [Not public]/

## 📁 What's Here

This folder contains the original project structure before the reorganization.

```
Lambda Driver/
├── qwen_setup/              # version 1.0.1 simple setup
│   ├── qwen_coder.py       # Basic Qwen interface
│   ├── install.bat         # version 1.0.1 installation
│   ├── run.bat             # version 1.0.1 runner
│   └── requirements.txt    # Dependencies
│
├── hybrid_llm/             # version 1.0.1 hybrid system
│   ├── main.py             # version 1.0.1 main entry
│   ├── rag_coder.py        # version 1.0.1 RAG implementation
│   ├── web_search.py       # Web search
│   ├── network_monitor.py  # Offline verification
│   ├── config.json         # version 1.0.1 config
│   └── ...                 # Other files
│
├── PROJECT_OVERVIEW.md     # version 1.0.1 documentation
├── TROUBLESHOOTING.md      # version 1.0.1 troubleshooting
├── CHANGELOG.md            # version 1.0.1 changelog
├── SETUP_COMPLETE.md       # version 1.0.1 setup guide
├── MODEL_MANAGEMENT.md     # version 1.0.1 model management
├── check_models.py         # Model checker
├── download_models.bat     # version 1.0.1 downloader
└── download_models.py      # version 1.0.1 downloader (Python)
```

## 🚫 Why This Was Replaced

### Problems with version 1.0.1 Structure

1. **Two Models (1.5B + 7B)**
   - Confusing which to use
   - Wasted disk space (~10GB)
   - Different quality levels

2. **Fixed Storage Location**
   - Models in system cache
   - Hard to manage
   - Can't choose drive

3. **Mixed Setup/Runtime**
   - Setup and run combined
   - Scripts tried to download during run
   - Got stuck frequently

4. **Windows Only**
   - No Linux support
   - Platform-specific

5. **Complex Structure**
   - Files scattered
   - Hard to understand
   - Difficult to maintain

## ✅ New Structure Benefits

See `../NEW_STRUCTURE/` for:

- ✅ Single 7B model (better quality)
- ✅ User-choice drive (D:\, E:\, etc.)
- ✅ Separate setup/runtime
- ✅ Windows + Linux support
- ✅ Clean, modular design

## 📖 Migration Guide

See `../NEW_STRUCTURE/MIGRATION_GUIDE.md` for:
- How to migrate from version 1.0.1 to new
- Step-by-step instructions
- Configuration mapping
- Troubleshooting

## 🗑️ Should You Delete This?

**Keep it if:**
- You want to reference version 1.0.1 code
- You're still using the version 1.0.1 structure
- You want to compare implementations

**Delete it if:**
- You've successfully migrated to NEW_STRUCTURE
- You need disk space
- You don't need the reference

## 📊 Comparison

| Feature | Lambda Driver | NEW_STRUCTURE |
|---------|---------------|---------------|
| Models | 1.5B + 7B | Only 7B |
| Storage | System cache | User choice |
| Setup | Combined | Separate |
| Platform | Windows | Windows + Linux |
| Download | During run | During setup |
| Structure | Mixed | Clean modules |

## 🔄 How to Use version 1.0.1 Structure (Not Recommended)

If you still want to use the version 1.0.1 structure:

```bash
cd Lambda Driver/qwen_setup
install.bat
run.bat
```

Or:

```bash
cd Lambda Driver/hybrid_llm
install.bat
run.bat
```

**Note:** This is not maintained and may have issues. 

## 📝 Version History

- **v1.0.0** - Initial release (Jan 18, 2026)
- **v1.0.1** - Fixed bitsandbytes dependency (Jan 18, 2026)
- **v2.0.0** - Replaced by version 2.0.0 (Jan 19, 2026)  "not public , currently in devlopment"

## 🆘 Support

For the version 1.0.1 structure:
- Check documentation in this fversion 1.0.1er
- See TROUBLESHOOTING.md
- See PROJECT_OVERVIEW.md

---

**Status:** Archived  
**Maintained:** No  
**Use:** Reference only  
**Recommended:** Use NEW_STRUCTURE instead

