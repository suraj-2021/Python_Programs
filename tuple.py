#Buffet: A buffet-style restaurant offers only four basic foods. Adding the food items store them in a tuple.

#creating a tuple
buffet_items = ('Paneer Tikka', 'Veg Biryani','Spnich and Feta Stuffed Mushrooms','Chana Masala')
#using for loop to print each item in the buffet
for item in buffet_items:
    print(item)

#the restaurant changed it's item and have to change the items on the tuple.
#we can't add a new item to the tuple but have to a new value to the same variable.
buffet_items = ('Paneer Tikka','Matar Paneer','Samosa','Palak Paneer')
for item in buffet_items:
     print(item)
