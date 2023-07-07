"""Unit tests for translator"""
import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """Class to test English to French translation code"""
    def test1(self):
        """english_to_french method test"""
        self.assertEqual(english_to_french("hello"), "bonjour") # "Hello" input = output "Bonjour"
class TestF2E(unittest.TestCase):
    """Class to test French to English translation code"""
    def test1(self):
        """french_to_english method test"""
        self.assertEqual(french_to_english("bonjour"), "hello") # "Bonjour" in "Hello" out

unittest.main()
