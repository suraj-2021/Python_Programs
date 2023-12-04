#This is a Polling program where user will input their 'name' and name of a mountain that they want to climb one day.
#We will store the name and mountain name inside the dictionary

poll = {}

poll_active = True

while poll_active:
      name = input("\n Please Enter your Name: ")
      mountain = input("\n Mountain name you want to climb: ")
      poll[name] = mountain
      active = input("\n Do you want other people to take this poll (yes/no)").title()
      if active == 'No':
         poll_active=False
print(poll)
