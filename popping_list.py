#Making a list of names including many names. Later removing the names and check the lis is empty, if list is empty print an appropirate message.

names = ['Shree','Krishna','Govinda','Hare','Murare','Admin']

for i in names:
    names.pop()
    
    if names:
       print("Hi")
    else:
        print("Need More names for the list")
    print(names)
