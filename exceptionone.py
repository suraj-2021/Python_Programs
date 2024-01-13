try:
    x = 1 / 'a'
except ZeroDivisionError:
    print("You can't divide by zero!")
except TypeError:
    print("Unsupported operand type!")
