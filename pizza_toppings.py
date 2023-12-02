#Using while loop to prompt Pizza toppings to user, later printing the pizza toppings

pro = "Hello please order the toppings: "
pro =  pro + "(Enter 'quit' to exit the loop)"

pizza_toppings=[]

while True:
      topping = input(pro)
      if topping == 'quit':
         break
      else:
          pizza_toppings.append(topping)
for pizza in pizza_toppings:
    print(f"Your ordered toppings are, {pizza}")
    
