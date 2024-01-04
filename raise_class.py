class Employee:
    raise_amount = 1.04  # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('John', 'Doe', 50000)
emp1.apply_raise()
print(emp1.pay)
