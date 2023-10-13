"""tests"""
import unittest
from make import read_magnets


class TestMake(unittest.TestCase):
    """Tests for make.py"""

    def test_read_magnets(self):
        """Tests reading magnets from a file"""

        file_contents = """text;count
Hello World;1
Foo Bar;2
"""
        magnets = read_magnets(file_contents)
        self.assertEqual(len(magnets), 3)
        self.assertEqual(magnets[0].label, "Hello World")
        self.assertEqual(magnets[1].label, "Foo Bar")
        self.assertEqual(magnets[2].label, "Foo Bar")
