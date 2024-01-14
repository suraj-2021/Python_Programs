while True:
    try:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.")
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
