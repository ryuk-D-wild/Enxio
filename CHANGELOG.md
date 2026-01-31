# Changelog

All notable changes to this project will be documented in this file.

## [1.0.1] - 2026-01-18

### Fixed
- **CRITICAL:** Added missing `bitsandbytes>=0.43.0` dependency
  - Error: `PackageNotFoundError: No package metadata was found for bitsandbytes`
  - Solution: Updated all requirements.txt and install.bat files
  - Both qwen_setup and hybrid_llm now install bitsandbytes automatically

### Added
- `TROUBLESHOOTING.md` - Comprehensive troubleshooting guide
- `CHANGELOG.md` - This file to track changes
- Better error documentation in PROJECT_OVERVIEW.md

### Changed
- Updated `qwen_setup/requirements.txt` - Added bitsandbytes>=0.43.0
- Updated `hybrid_llm/requirements.txt` - Added bitsandbytes>=0.43.0
- Updated `qwen_setup/install.bat` - Now installs bitsandbytes
- Updated `hybrid_llm/install.bat` - Now installs bitsandbytes
- Updated `PROJECT_OVERVIEW.md` - Added bitsandbytes error to troubleshooting

### Installation Status
- ✅ qwen_setup: Fully installed with all dependencies
- ✅ hybrid_llm: Fully installed with all dependencies
- ✅ bitsandbytes: Installed in both environments

---

## [1.0.0] - 2026-01-18

### Initial Release

#### Created Systems
1. **qwen_setup/** - Simple Qwen interface
   - Basic chat functionality
   - Optimized for low-end hardware
   - 4-bit quantization support

2. **hybrid_llm/** - Full hybrid system
   - RAG (Retrieval-Augmented Generation)
   - Web search integration
   - Network monitoring (offline verification)
   - Fine-tuning support via Colab
   - Configuration system

#### Core Features
- Local LLM execution (Qwen 2.5 Coder)
- Offline operation with verification
- Novel code generation from patterns
- Codebase indexing and search
- Web search for documentation
- Fine-tuning pipeline for Colab/Kaggle
- Fits in 50GB storage constraint
- Optimized for 2-core CPU

#### Documentation
- `PROJECT_OVERVIEW.md` - Complete project documentation
- `QUICKSTART.md` - Quick start guide
- `README.md` files for each component
- Colab training notebook
- Installation scripts for Windows

#### Components
- `rag_coder.py` - RAG implementation
- `web_search.py` - DuckDuckGo search integration
- `network_monitor.py` - Offline verification
- `main.py` - Main entry point
- `test_system.py` - System diagnostics
- `quick_test.py` - Quick model test
- `load_finetuned.py` - Load trained models
- `colab_training.ipynb` - Training notebook

#### Configuration
- `config.json` - System configuration
- Model selection (0.5B to 7B)
- RAG settings
- Generation parameters
- Network settings

---

## Installation Commands

### Fresh Install
```bash
# Simple version
cd qwen_setup
install.bat

# Full system
cd hybrid_llm
install.bat
```

### Update Existing Installation
```bash
# If you installed before 2026-01-18, run:
qwen_setup\venv\Scripts\python.exe -m pip install bitsandbytes>=0.43.0
hybrid_llm\venv\Scripts\python.exe -m pip install bitsandbytes>=0.43.0
```

---

## Known Issues

### Current
- None

### Resolved
- ✅ Missing bitsandbytes dependency (Fixed in 1.0.1)

---

## Roadmap

### Planned Features
- [ ] Better RAG with semantic search (sentence-transformers)
- [ ] Multi-language support beyond English
- [ ] GUI interface option
- [ ] Docker containerization
- [ ] Automatic model selection based on RAM
- [ ] Progress bars for model download
- [ ] Code execution sandbox
- [ ] Git integration for codebase tracking

### Under Consideration
- [ ] GPU support (CUDA/ROCm)
- [ ] API server mode
- [ ] VS Code extension
- [ ] Collaborative features
- [ ] Cloud sync for fine-tuned models

---

## Version History

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| 1.0.1 | 2026-01-18 | Current | Fixed bitsandbytes dependency |
| 1.0.0 | 2026-01-18 | Stable | Initial release |

---

**Maintained by:** Project Team
**Last Updated:** January 18, 2026
