user_input = input("Enter a number in the range of 1 through 7: ")

if user_input.isdigit():
    user_input = int(user_input)
    
    if 1 <= user_input <= 7:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(f"The corresponding day of the week is {days_of_week[user_input - 1]}.")
    else:
        print("Error, out of range")
else:
    print("Error, invalid input. Please enter a valid number.")
