#The following function takes a list of names and great each person in the list.

def greet_users(names):
    for name in names:
       msge= f"Hello,{name.title()}!"
       print(msge)
       
user_names=['Shree','Krishna','Govinda','Hare']

greet_users(user_names)
