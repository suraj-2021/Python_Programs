# Parent class
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

# Child class
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self._employee_id = employee_id

# Create an instance of Employee
employee = Employee("John", 30, "E123")
print(employee._name)  # Outputs: John
print(employee._employee_id)  # Outputs: E123
