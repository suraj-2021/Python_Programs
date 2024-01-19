# This is your function
def add_numbers(a, b):
    return a + b

# This is your test
import unittest

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-1, -1), -2)

# This is your test runner
if __name__ == '__main__':
    unittest.main()
