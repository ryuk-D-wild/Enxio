"""
Network Monitor - Verify Qwen runs offline with no data leaks
"""

import socket
import sys
from contextlib import contextmanager


class NetworkBlocker:
    """Block all network access to verify offline operation."""
    
    def __init__(self):
        self.original_socket = None
        self.blocked = False
    
    def block(self):
        """Block all network connections."""
        if self.blocked:
            return
        
        self.original_socket = socket.socket
        
        def blocked_socket(*args, **kwargs):
            raise RuntimeError(
                "🚫 NETWORK ACCESS BLOCKED!\n"
                "The model tried to connect to the internet.\n"
                "This should NOT happen in offline mode."
            )
        
        socket.socket = blocked_socket
        self.blocked = True
        print("✅ Network blocker activated - Model is offline")
    
    def unblock(self):
        """Restore network access."""
        if not self.blocked:
            return
        
        socket.socket = self.original_socket
        self.blocked = False
        print("🌐 Network access restored")


@contextmanager
def offline_mode():
    """Context manager for offline operation."""
    blocker = NetworkBlocker()
    try:
        blocker.block()
        yield blocker
    finally:
        blocker.unblock()


def verify_offline():
    """Test that network blocking works."""
    print("\n" + "=" * 60)
    print("Testing Network Blocker...")
    print("=" * 60)
    
    blocker = NetworkBlocker()
    blocker.block()
    
    try:
        # Try to make a connection (should fail)
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("❌ FAILED: Network is still accessible!")
        return False
    except RuntimeError as e:
        print("✅ SUCCESS: Network is blocked")
        print(f"   Error message: {str(e)[:50]}...")
        return True
    finally:
        blocker.unblock()


if __name__ == "__main__":
    verify_offline()
