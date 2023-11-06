#Creating a list of Guests living or deceased, coming for my dinner. Later adding some more guests to the list using multiple methods.

#Creating a List
guests = ['Shree','Krishna','Govinda','Hare','Murare','Hey','Natha','Narayana' 'Vashudeva']

#Adding new names to the list
guests.insert(0,'Shiva')
guests.insert(4,'Gangadhar')
guests.insert(10,'Neel Kantha')

#Printing the new list
print(guests)

#printing one message each for the name in the list
for guest in guests:
    print(f" Namaste {guest}, I'm inviting you to the dinner tonight")
