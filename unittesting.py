# This is your function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# This is your test
import unittest

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

# This is your test runner
if __name__ == '__main__':
    unittest.main()
