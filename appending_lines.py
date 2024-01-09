"""Reading in each line from the file I just created, and 
replace the word python with the name of another language, such as JavaScript. Print 
each modified line to the screen."""

with open('python_learnings.txt') as main_file:
    x_file = main_file.readlines()
    my_list=[]
    for line in x_file:
        my_list.append(line.replace('python','Javascript'))
        
        

print(my_list)

print(f"\n\n{my_list[3:5]}")
