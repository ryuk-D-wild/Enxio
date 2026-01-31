"""
Test script to verify everything works
"""

import sys
from pathlib import Path


def test_imports():
    """Test if all dependencies are installed."""
    print("Testing imports...")
    
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__}")
    except ImportError:
        print("❌ PyTorch not installed")
        return False
    
    try:
        import transformers
        print(f"✅ Transformers {transformers.__version__}")
    except ImportError:
        print("❌ Transformers not installed")
        return False
    
    try:
        import requests
        print("✅ Requests")
    except ImportError:
        print("⚠️  Requests not installed (web search won't work)")
    
    return True


def test_config():
    """Test if config file exists."""
    print("\nTesting configuration...")
    
    if not Path("config.json").exists():
        print("❌ config.json not found")
        return False
    
    import json
    with open("config.json") as f:
        config = json.load(f)
    
    print(f"✅ Model: {config['model']['name']}")
    print(f"✅ RAG path: {config['rag']['codebase_path']}")
    print(f"✅ Offline mode: {config['network']['offline_mode']}")
    
    return True


def test_network_blocker():
    """Test network blocking."""
    print("\nTesting network blocker...")
    
    try:
        from network_monitor import verify_offline
        result = verify_offline()
        return result
    except Exception as e:
        print(f"❌ Network blocker test failed: {e}")
        return False


def test_model_download():
    """Check if model needs to be downloaded."""
    print("\nChecking model cache...")
    
    import os
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"
    
    if cache_dir.exists():
        models = list(cache_dir.glob("models--Qwen*"))
        if models:
            print(f"✅ Found {len(models)} Qwen model(s) in cache")
            return True
    
    print("⚠️  No cached models found")
    print("   First run will download ~6GB")
    return True


def main():
    """Run all tests."""
    print("=" * 70)
    print("Hybrid LLM System - Pre-flight Check")
    print("=" * 70)
    
    tests = [
        ("Dependencies", test_imports),
        ("Configuration", test_config),
        ("Network Blocker", test_network_blocker),
        ("Model Cache", test_model_download),
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\n{'=' * 70}")
        result = test_func()
        results.append((name, result))
    
    print("\n" + "=" * 70)
    print("Summary:")
    print("=" * 70)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
        if not result:
            all_passed = False
    
    print("=" * 70)
    
    if all_passed:
        print("\n✅ All tests passed! Run 'run.bat' to start.")
    else:
        print("\n❌ Some tests failed. Check errors above.")
        print("   Run 'install.bat' if dependencies are missing.")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
