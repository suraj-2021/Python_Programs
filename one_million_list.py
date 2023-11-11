#Creating a list using for loop to store numbers from 1 to 1000000 and printing each number.

#assigning a variable
one_million = [million for million in range(1,1000001)]
for number in one_million:
    print(number)
