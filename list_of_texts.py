#We are accessing a text file and read through that file. Later we append each line of the text to a list and we print that list.

with open('python_learnings.txt') as main_file:
    x_file = main_file.readlines()
    i_list = []
    for line in x_file:
        i_list.append(line)

print(x_file)

print(f"\n\n{x_file[3:5]}")
        
    
