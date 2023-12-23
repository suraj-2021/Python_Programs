#Creating a Class that takes User information as attributes and later using these attributes prints meaningful data.

class User:
    def __init__(self,first_name,last_name,age,sex,address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.address = address
    
    def describe_user(self):
        user = f"\nFull Name : {self.first_name} {self.last_name},\n {self.age} years old, \n{self.sex}, \n{self.address}"
        print(user)
    
    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}!!")

    
user1 = User('Narayana','Dasa','24','Male','Vrindavan')
user2 = User('Neel', 'Kanth','0','Male','Kailasa')

user1.describe_user()
user1.greet_user()
 
user2.describe_user()
user2.greet_user()

