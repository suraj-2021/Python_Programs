# Parent classes
class Father:
    def gardening(self):
        return "I enjoy gardening."

class Mother:
    def cooking(self):
        return "I love to cook."

# Child class
class Child(Father, Mother):
    pass

# Create an instance of Child
child = Child()
print(child.gardening())  # Outputs: I enjoy gardening.
print(child.cooking())  # Outputs: I love to cook.
