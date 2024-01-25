import unittest

class StringManipulator:
    def reverse(self, string):
        return string[::-1]

    def is_palindrome(self, string):
        return string == string[::-1]

class TestStringManipulator(unittest.TestCase):
    def test_reverse(self):
        manipulator = StringManipulator()
        self.assertEqual(manipulator.reverse("hello"), "olleh")

    def test_is_palindrome(self):
        manipulator = StringManipulator()
        self.assertTrue(manipulator.is_palindrome("racecar"))
        self.assertFalse(manipulator.is_palindrome("hello"))

if __name__ == '__main__':
    unittest.main()
