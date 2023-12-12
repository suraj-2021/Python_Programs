#An arbitary number of arguments

def pizza_toppings(*toppings):
    #this *toppings parameter stores as many argument a user passes
    print(toppings)
    
pizza_toppings('mushroom')
pizza_toppings('olives','extra cheese','onion')
