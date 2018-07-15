#!/usr/bin/env python3
"""
Tests for the ASCII mime.
"""
import unittest
from asciimime import text_to_emoticon


class TestTextToEmoticon(unittest.TestCase):
    """
    Test the text/toot to emoticon conversion.
    """

    def test_positive(self):
        """generic positive case"""
        res = text_to_emoticon("this is fun!")
        self.assertEqual(res, ':)')

    def test_negative(self):
        """generic negative case"""
        res = text_to_emoticon("this is bad!")
        self.assertEqual(res, ':(')


if __name__ == '__main__':
    unittest.main()
