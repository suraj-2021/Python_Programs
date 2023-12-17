#A class that returns the average grade of a student
class Student:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades
        
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
