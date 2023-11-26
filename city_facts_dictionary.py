#Create a dictionary where key is a city name and value is another dictionary containg city Facts.

cities = {'Kathmandu':{'Country':'Nepal','Population':'3million','Fact':'City of Hindu Community Centers'}}

#looping through the dictionary
for city in cities:
    print(f"The city we are discussing is {city}")

#printing the values of the nested dictionary containing city facts.
for city in cities.items():
    x = city[1].values()

for y in x:
    print
    
