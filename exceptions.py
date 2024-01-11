#I have written two programmes one programme is not designed for handling exceptions where the second programme is designed for handling exceptions.

print("Give me Two numbers and i'll divide them.")
print("Type q to quit")

while True:
    first_number = input("First number: ")
    
    if first_number == 'q':
       break
    
    second_number = input("Second number: ")
    
    if second_number == 'q':
       break
    
    else:
        print(int(first_number)/int(second_number))
        
        
        
print("Give me Two numbers and i'll divide them.")
print("Type q to quit")

while True:
    first_number = input("First number: ")
    
    if first_number == 'q':
       break
    
    second_number = input("Second number: ")
    
    if second_number == 'q':
       break
    try:
       answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
           print("Cant divide by zero!")
    else:
        print(answer)
        
