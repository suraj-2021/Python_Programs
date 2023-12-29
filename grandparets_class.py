# Parent class
class Grandparent:
    def __init__(self, name):
        self.name = name

# Intermediate class
class Parent(Grandparent):
    def hobby(self):
        return "I like reading books."

# Child class
class Child(Parent):
    pass

# Create an instance of Child
child = Child("John")
print(child.name)  # Outputs: John
print(child.hobby())  # Outputs: I like reading books.
