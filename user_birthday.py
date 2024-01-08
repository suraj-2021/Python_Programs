"""Opening a file. Reading the file. Appending the content of that file to new string. Printing that string. Taking input from user about his birthday. Checking if user's birthday in the file. If birthday is present in the file tell user about it, if birthday is not present tell user that too."""
filename = 'million_random_digits.py'

with open(filename) as file:
    
    lines = file.readlines()

digi_string = ''
for line in lines:
    digi_string +=line.strip()

birthday = int(input("Please Enter your birthday as mmddyy: "))
if birthday in lines:
    print("Your birthday is in milloon random digits!!")
else:
    print("Your birthday is not there in this file")
