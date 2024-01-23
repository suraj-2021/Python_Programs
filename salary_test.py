class Employee:
    def __init__(self,first_name,last_name, annual_salary):
        self.first_name= first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    def give_raise(self,amount=0):
        self.annual_salary = self.annual_salary + amount
        print(self.annual_salary)

    

x = Employee('suraj','sharma',120000)

x.give_raise()


#testing this code
import unittest
from. import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.f_name = 'Bharat'
        self.l_name = 'Raja'
        self.a_salary = 100000000
        
    def test_default_salary_raise():
        x = Employee(self.f_name,self.l_name,self.a_salary)
        x.give_raise()

