@echo off
echo ========================================
echo Qwen Model Downloader
echo ========================================
echo.
echo This will download models to:
echo %USERPROFILE%\.cache\huggingface\hub\
echo.
echo Models will be cached and reused
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

echo Choose which model to download:
echo.
echo 1. Qwen 1.5B (~3GB) - For qwen_setup
echo 2. Qwen 7B (~7GB) - For hybrid_llm
echo 3. Both models (~10GB total)
echo.
set /p choice="Enter choice (1/2/3): "

if "%choice%"=="1" goto download_1_5b
if "%choice%"=="2" goto download_7b
if "%choice%"=="3" goto download_both
echo Invalid choice
pause
exit /b 1

:download_1_5b
echo.
echo Downloading Qwen 1.5B...
python -c "from huggingface_hub import snapshot_download; import os; snapshot_download('Qwen/Qwen2.5-Coder-1.5B-Instruct', cache_dir=os.path.expanduser('~/.cache/huggingface/hub'))"
echo.
echo Done! Model cached.
goto end

:download_7b
echo.
echo Downloading Qwen 7B...
python -c "from huggingface_hub import snapshot_download; import os; snapshot_download('Qwen/Qwen2.5-Coder-7B-Instruct', cache_dir=os.path.expanduser('~/.cache/huggingface/hub'))"
echo.
echo Done! Model cached.
goto end

:download_both
echo.
echo Downloading Qwen 1.5B...
python -c "from huggingface_hub import snapshot_download; import os; snapshot_download('Qwen/Qwen2.5-Coder-1.5B-Instruct', cache_dir=os.path.expanduser('~/.cache/huggingface/hub'))"
echo.
echo Downloading Qwen 7B...
python -c "from huggingface_hub import snapshot_download; import os; snapshot_download('Qwen/Qwen2.5-Coder-7B-Instruct', cache_dir=os.path.expanduser('~/.cache/huggingface/hub'))"
echo.
echo Done! Both models cached.
goto end

:end
echo.
echo ========================================
echo Models cached at:
echo %USERPROFILE%\.cache\huggingface\hub\
echo.
echo You can now run:
echo   qwen_setup\run.bat
echo   hybrid_llm\run.bat
echo ========================================
pause
