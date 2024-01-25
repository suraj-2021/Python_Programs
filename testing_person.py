import unittest

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class TestPerson(unittest.TestCase):
    def test_person(self):
        person = Person("John", 30)
        self.assertEqual(person.name, "John")
        self.assertEqual(person.age, 30)

if __name__ == '__main__':
    unittest.main()
