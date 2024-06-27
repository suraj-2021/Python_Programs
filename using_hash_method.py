class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        # Compute the hash based on the person's name
        return hash(self.name)


alice = Person(name="Alice", age=30)
bob = Person(name="Bob", age=28)

# A set of people
people_set = {alice, bob}

#if Alice is in the set
print("Is Alice in the set?", alice in people_set)
