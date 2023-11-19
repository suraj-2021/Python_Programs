#Checking if new username is already in current user list, if it is prompt user to provide another username.

current_users = ["Shree","Krishna","Govinda","Hare","Murare"]
current_users_lower = []
current_users_upper = []

for i in current_users:
    current_users_lower.append(i.lower())
    current_users_upper.append(i.upper())

new_users = ["Hey","Natha","Narayana","Govinda","Krishna"]

for name in new_users:
    if name in current_users:
       print(f"{name}Not Available")
    if name.upper() in current_users_upper:
       print(f"{name}Name not Available")
    if name.lower() in current_users_lower:
       print(f"{name}Name not available")
