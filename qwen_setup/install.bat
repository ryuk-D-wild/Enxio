@echo off
echo ========================================
echo Qwen Coder Setup for Windows
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python 3.10+ from https://python.org
    pause
    exit /b 1
)

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing PyTorch (CPU version for low-end hardware)...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

echo Installing other dependencies...
pip install transformers>=4.37.0 accelerate bitsandbytes>=0.43.0 sentencepiece protobuf huggingface-hub

echo.
echo ========================================
echo Downloading Qwen 1.5B Model...
echo ========================================
echo This will download ~3GB to cache
echo Model will be reused, only downloads once
echo.

python -c "from huggingface_hub import snapshot_download; import os; print('Downloading Qwen 1.5B...'); snapshot_download('Qwen/Qwen2.5-Coder-1.5B-Instruct', cache_dir=os.path.expanduser('~/.cache/huggingface/hub')); print('Download complete!')"

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo Model cached at: %USERPROFILE%\.cache\huggingface\hub\
echo.
echo To run Qwen Coder:
echo   1. Run: run.bat
echo.
pause
