#start out with list of Unverified users and later moving these to the new list of confirmed users.
unverified_list = ['Shree','Krishna','Govind','Hare','Murare']

verified_list = []

while unverified_list:
      current_user = unverified_list.pop()
      print(f"\n Currently verifying {current_user.title()}")
      verified_list.append(current_user)

for i in verified_list:
    print(f"\nVerified Users:  {i}")
