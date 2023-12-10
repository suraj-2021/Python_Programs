#Building a city with a function that takes park name and street name as argument and returns a dictionary.

def build_city(park_name,street_name):
    city ={'park': park_name, 'street': street_name}
    return city
    

print(build_city('rose park', 'downtown street'))

print(build_city('yellow garden', 'mainway street'))


