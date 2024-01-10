#Taking input from users and writing that input to the and later displaying what's been written.
filename = 'guests.txt'
with open(filename,'r+') as file_obj:
    y = input("Please enter your name here: ")
    file_obj.write(f"{y}\n")
    z = file_obj.read()

print(z)
