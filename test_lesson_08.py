import unittest

# Assuming the student's code is imported from lesson_08.py
from lesson_08 import calculate_circle_area, square, is_even, multiply

class TestLesson08(unittest.TestCase):
    def test_calculate_circle_area(self):
        self.assertAlmostEqual(calculate_circle_area(5), 78.5, places=1)

    def test_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(-3), 9)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
