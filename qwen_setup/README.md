# Qwen Coder - Local Setup

## Quick Start

1. Double-click `install.bat` (first time only)
2. Double-click `run.bat` to start

## Model Selection (Edit qwen_coder.py)

Pick based on your RAM:

| Model | RAM Needed | Quality |
|-------|-----------|---------|
| Qwen2.5-Coder-0.5B | ~2GB | Basic |
| Qwen2.5-Coder-1.5B | ~4GB | Good (default) |
| Qwen2.5-Coder-3B | ~6GB | Better |
| Qwen2.5-Coder-7B | ~10GB | Best for local |

## Maximizing Accuracy

The code is already optimized, but you can tweak:

- **temperature**: Lower = more accurate (0.1), Higher = more creative (0.7)
- **System prompt**: Edit `_get_system_prompt()` for your use case
- **Model size**: Bigger model = better accuracy (if RAM allows)

## Honest Truth

Even with all optimizations, Qwen-7B is roughly:
- 10-20% of Sonnet's capability on complex reasoning
- 40-60% on straightforward coding tasks
- Good for: boilerplate, simple functions, explanations
- Weak on: complex architecture, subtle bugs, multi-file context
