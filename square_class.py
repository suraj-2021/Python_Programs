# Parent class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Child class
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Create an instance of Square
square = Square(4)
print(square.area())  # Outputs: 16
