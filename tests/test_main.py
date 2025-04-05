import unittest
from main import greet, is_even, max_of_two

class TestFunctionBasics(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))

    def test_max_of_two(self):
        self.assertEqual(max_of_two(5, 3), 5)
        self.assertEqual(max_of_two(4, 4), 4)
        self.assertEqual(max_of_two(-1, -5), -1)

if __name__ == "__main__":
    unittest.main()
