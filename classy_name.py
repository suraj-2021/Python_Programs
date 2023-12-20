class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create an instance of the Person class
p = Person("Alice", 25)

# Use the greet method
print(p.greet())
