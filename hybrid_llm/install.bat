@echo off
echo ========================================
echo Hybrid LLM System Setup
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Install from: https://python.org
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
python -m venv venv

echo [2/5] Activating environment...
call venv\Scripts\activate.bat

echo [3/5] Installing PyTorch (CPU version)...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

echo [4/5] Installing transformers and dependencies...
pip install transformers>=4.37.0 accelerate bitsandbytes>=0.43.0 sentencepiece protobuf huggingface-hub

echo [5/5] Downloading Qwen 7B model...
echo This will download ~7GB to cache
echo Model will be reused, only downloads once
echo.

python -c "from huggingface_hub import snapshot_download; import os; print('Downloading Qwen 7B...'); snapshot_download('Qwen/Qwen2.5-Coder-7B-Instruct', cache_dir=os.path.expanduser('~/.cache/huggingface/hub')); print('Download complete!')"

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo Model cached at: %USERPROFILE%\.cache\huggingface\hub\
echo.
echo IMPORTANT: First run will load model from cache (fast)
echo.
echo To start:
echo   run.bat
echo.
pause
