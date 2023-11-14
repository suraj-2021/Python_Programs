#Creating a original list of Pizzas and create a copy of it, and do multiple slicing operations.

#creating a list of pizzas
my_pizzas = ['Margherita','Golden Corn','Jalapeno','Double Cheese Margherita','Crisp Caspsicum']

#creating it's copy and assigning it to new variable
your_pizzas = my_pizzas[:]

#adding new pizzas to my_pizzas and printing the list.
my_pizzas.append('Onion')
my_pizzas.append('Farmhouse')
print(my_pizzas)

#adding new pizzas to your_pizzas and printing the list.
your_pizzas.append('Argula-Almond')
your_pizzas.append('Butternut Squash')
print(your_pizzas)
