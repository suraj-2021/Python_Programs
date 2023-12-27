#Creating a User class, where i will pass a default attribute and perform all sorts of operations on it. For example i will increment the default attribute using a method and i will also reset thee login attempts again. I will reset the default attribute.
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 2
    #Printing the user details
    def user_details(self):
        full_name = f"{self.first_name} {self.last_name}"
        return print(full_name.title())
    #incrementing the default attribute    
    def increment_login_attempts(self):
        self.login_attempts +=1
        print(self.login_attempts)
    #reset login attempts
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)
        
   

user = User('Anil','Dhabi')
user.user_details()
user.increment_login_attempts()
user.reset_login_attempts()
