#Making a list of names including a name called "Admin". For Admin we will print a special message and for other names we will print a generic message.

names = ['Shree','Krishna','Govinda','Hare','Murare','Admin']

for name in names:
    if name == 'Admin':
       print("Hello Admin, Want to see the status?")
    else:
        print(f"Welcome back {name}, Thank you for loggin in again!")
