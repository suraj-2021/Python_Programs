import unittest

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

if __name__ == '__main__':
    unittest.main()
