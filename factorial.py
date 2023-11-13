#Calculting the factorial of a given number

n = int(input("Give me a Number:"))

list = [i for i in range(1,n+1)]
list.reverse()

j = 1
for i in list:
    j = j*i
print(f"The factorial of the number{n} is {j}")
