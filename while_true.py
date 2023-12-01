#If user enter exit he will end the program, else the program will run

while True:
    user_input = input("Enter a number: ")
    if user_input == "exit":
        break
    elif int(user_input) % 2 == 0:
        print(user_input, "is even.")
    else:
        print(user_input, "is odd.")
