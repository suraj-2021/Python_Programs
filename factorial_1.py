# This is a Python program to calculate factorial

def factorial(n):
    """
    This function calculates the factorial of a number.
    
    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the number.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

# Test the function
print(factorial(5))  # Output: 120
