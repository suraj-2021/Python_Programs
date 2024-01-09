#We are accessing a text file and reading line by line through that file. Later we print the contents using for loop.

with open('python_learnings.txt') as main_file:
    x_file = main_file.readlines()
    
    for line in x_file:
        print(f"\n{x_file}")
        
    
"""print(x_file)
print(f"\n{x_file}")
print(f"\n{x_file}")
print(f"\n{x_file}")
print(f"\n{x_file}")"""
