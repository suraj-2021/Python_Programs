#Creating a dictionary, the value is another dictionary.

users = {'aledison':{'first':'Thomas','middle':'Alva','last':'Edison'},'mfarade':{'first':'Michael','last':'Farady'}}

for name,values in users.items():
    print(f"He is a Scientist and His User_Name is {name}")
    print(f"His real name is {name['first']} {name['last']}")
    
