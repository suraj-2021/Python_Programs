#Odd Numbers: Using the third argument of the range() function to make a list of the odd numbers from 1 to 20. Using a for loop to print each number.

#creating a list using the third argument of the range() function
odd_numbers = [odd for odd in range(1,20,2)]

#using a for loop to print each number
for odd in odd_numbers:
    print(odd)
