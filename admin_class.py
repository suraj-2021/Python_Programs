#Creating a class called User, later creating another class called Admin which inherits the initial User class.
# the Admin class will describe the Admin privileges 
class User:
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def describe_user(self):
        print(f"User name is {self.name}, User age is {self.age}, User is from {self.place}")
        

class Admin(User):
    def __init__(self,name,age,place,task):
        super().__init__(name,age,place)
        self.task = task
        self.privileges = ['can post','can delete post','can update post','can ban user']
    
    def show_privileges(self):
        for p in self.privileges:
            print(f"\n{p}")
            

my_admin = Admin('Shiv','infinite','Kailash','Destroyer of sorrows')

my_admin.describe_user()

my_admin.show_privileges()
