#Remving items from one list and shiftig them to others
sandwich_orders = ['aloo sandwich','Mooli Sandwich','Cheese Sandwich','Onion Sandwich','Italian Sandwich','Nepali Sandwich']

finished_sandwiches = []

for sandwich in sandwich_orders:
    popped_sandwich = sandwich_orders.pop(sandwich_orders.index(sandwich))
    print(f"Now preparing {popped_sandwich} for you!")
    finished_sandwiches.append(popped_sandwich)
print(finished_sandwiches)
    
