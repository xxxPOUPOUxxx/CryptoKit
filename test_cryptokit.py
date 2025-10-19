# test_cryptokit.py
"""
Tests for CryptoKit module.
"""

import unittest
from cryptokit import CryptoKit

class TestCryptoKit(unittest.TestCase):
    """Test cases for CryptoKit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoKit()
        self.assertIsInstance(instance, CryptoKit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoKit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
