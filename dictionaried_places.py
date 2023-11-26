#Creating dictionary where each key is person's name and value is a list containing person's favorite places to visit.
favorite_places = {
 'Shree': ['Gokul', 'Vrindavaan'],
 'Krishna': ['Dwarka','Puri','Vrindaavan'],
 'Govind': ['Mathura', 'Vaikuntha'],
 'Hare': ['Vaikuntha', 'Nirvanpuri'],
 }

#looping through our dictionary and printing values
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
