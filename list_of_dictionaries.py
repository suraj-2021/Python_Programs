#Creating Dictionaries and storing them in a list later loping through the list and printing the content in dictionaries.
my_stuff1 = {'computer':'lenovo','keyboard':'Apple','Mouse':'Microsoft','Version':20}
my_stuff2 = {'Phone':'Apple','Earphones':'Boat','Charger':'Apple 15 pro max', 'Version':15}

listed_stuffs = [my_stuff1,my_stuff2]

for s in listed_stuffs:
    stuff = s.items()
    print(stuff)
