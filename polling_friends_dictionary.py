#If a friend already taken the favorite language poll thank them, if not tell them to take the poll!

favorite_languages = {'Shree':'Tamil','Krishna':'Telugu','Govinda':'Kannad','Hare':'Orissi'}

polling_friends = ['Murare','Hae','Natha','Narayana','Govinda','Hare']

for i in polling_friends:
    if i in favorite_languages.keys():
       print(f"Hi {i} I See you've already taken the Poll, Thank you for taking the Poll!")
    else:
        print(f"Hello {i},Please take the Poll!")
