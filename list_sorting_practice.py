#Think of at least five places in the world you’d like to 
visit
#And perform various sorting oprations to the list.

#list of places i want to visit
places = ['New York', 'Las Vegas','Paris', 'Vanarashi','Puri']

#using sorted() method to print out the sorter version of the list without modifying the original list.
print(sorted(places))

#reversing the list using the reverse() method
places.reverse()
print(places)

#using reverse() method to reverse back the list to it's original form
places.reverse()
print(places)

#using sort to sort the list in alphabetical order
places.sort()
print(places)
      
#reversing the sorted list using sort() again
places.sort(reverse = True)
print(places)
