#Using two functions simulating the 3D model printing company.

def models_printing(unprinted_models,completed_models):
    while unprinted_models:
          current_model=unprinted_models.pop()
          print(f"The model {current_model} is being printed")
          completed_models.append(current_model)
          

def show_result(completed_models):
    for i in completed_models:
        print(f"\nCompleted printing 3D model of {i}!")
        
user_orders = ['Doraemon','Pikachu','Ninja Hatori','Goku']
completed_orders = []

models_printing(user_orders,completed_orders)
show_result(completed_orders)
