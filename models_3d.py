#Without using functions, simulate a task received to a 3d model printing company.
unfinisned_models = ['Phone Case','Robot Pendant','Blue Bird']
finished_models = []

while unfinisned_models:
    
      current_model = unfinisned_models.pop()
      print(f"Currently Printing {current_model}")
      finished_models.append(current_model)
     
for finished in finished_models:
    print(f"The model {finished} is completed!")
          
