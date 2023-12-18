class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def sit(self):
        print(f"{self.name} is sitting Now!")
        
    def roll_over(self):
        print(f"{self.name} is rolling over Now!")
    
  Dog.sit('hello',9)
