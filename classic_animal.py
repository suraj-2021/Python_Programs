# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I don't know what sound I make!"

# Child class
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Create an instance of Dog
dog = Dog("Rex")
print(dog.name)  # Outputs: Rex
print(dog.speak())  # Outputs: Woof!
