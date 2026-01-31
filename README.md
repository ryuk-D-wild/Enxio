# OLD STRUCTURE - Archive

## ⚠️ This is the OLD project structure

**Status:** Archived for reference only  
**Date Archived:** January 19, 2026  
**Replaced By:** NEW_STRUCTURE/

## 📁 What's Here

This folder contains the original project structure before the reorganization.

```
OLD_STRUCTURE/
├── qwen_setup/              # Old simple setup
│   ├── qwen_coder.py       # Basic Qwen interface
│   ├── install.bat         # Old installation
│   ├── run.bat             # Old runner
│   └── requirements.txt    # Dependencies
│
├── hybrid_llm/             # Old hybrid system
│   ├── main.py             # Old main entry
│   ├── rag_coder.py        # Old RAG implementation
│   ├── web_search.py       # Web search
│   ├── network_monitor.py  # Offline verification
│   ├── config.json         # Old config
│   └── ...                 # Other files
│
├── PROJECT_OVERVIEW.md     # Old documentation
├── TROUBLESHOOTING.md      # Old troubleshooting
├── CHANGELOG.md            # Old changelog
├── SETUP_COMPLETE.md       # Old setup guide
├── MODEL_MANAGEMENT.md     # Old model management
├── check_models.py         # Model checker
├── download_models.bat     # Old downloader
└── download_models.py      # Old downloader (Python)
```

## 🚫 Why This Was Replaced

### Problems with Old Structure

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
- How to migrate from old to new
- Step-by-step instructions
- Configuration mapping
- Troubleshooting

## 🗑️ Should You Delete This?

**Keep it if:**
- You want to reference old code
- You're still using the old structure
- You want to compare implementations

**Delete it if:**
- You've successfully migrated to NEW_STRUCTURE
- You need disk space
- You don't need the reference

## 📊 Comparison

| Feature | OLD_STRUCTURE | NEW_STRUCTURE |
|---------|---------------|---------------|
| Models | 1.5B + 7B | Only 7B |
| Storage | System cache | User choice |
| Setup | Combined | Separate |
| Platform | Windows | Windows + Linux |
| Download | During run | During setup |
| Structure | Mixed | Clean modules |

## 🔄 How to Use Old Structure (Not Recommended)

If you still want to use the old structure:

```bash
cd OLD_STRUCTURE/qwen_setup
install.bat
run.bat
```

Or:

```bash
cd OLD_STRUCTURE/hybrid_llm
install.bat
run.bat
```

**Note:** This is not maintained and may have issues.

## 📝 Version History

- **v1.0.0** - Initial release (Jan 18, 2026)
- **v1.0.1** - Fixed bitsandbytes dependency (Jan 18, 2026)
- **v2.0.0** - Replaced by NEW_STRUCTURE (Jan 19, 2026)

## 🆘 Support

For the old structure:
- Check documentation in this folder
- See TROUBLESHOOTING.md
- See PROJECT_OVERVIEW.md

For the new structure:
- See ../NEW_STRUCTURE/README.md
- See ../NEW_STRUCTURE/MIGRATION_GUIDE.md

---

**Status:** Archived  
**Maintained:** No  
**Use:** Reference only  
**Recommended:** Use NEW_STRUCTURE instead
