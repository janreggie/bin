"""Unit tests for verticalize.py"""
import unittest

from verticalize import verticalize


class TestVerticalize(unittest.TestCase):
    """Tests for the Verticalize function"""

    def test_verticalize(self):
        """Basic unit test"""
        input_str = "你好，世界！"
        width = 2
        expected_output = """世你
界好
！，"""
        self.assertEqual(verticalize(input_str, width), expected_output)
    
    def test_verticalize_with_offset(self):
        """What if width isn't even"""
        input_str = "你好，世界"
        width = 2
        expected_output = """世你
界好
　，"""
        self.assertEqual(verticalize(input_str, width), expected_output)



if __name__ == '__main__':
    unittest.main()
