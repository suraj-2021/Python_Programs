#Sum of even numbers upto the user input

def sum_of_even(numbers):
    total = 0
    for number in numbers:
        if number %2== 0:
           total=total+number
    return total
    

user_input = int(input("Give a number upto you want to count the sum of even numbers: ")) 

number_list = [i for i in range(user_input+1)]


total_sum = print(f"{sum_of_even(number_list)}")
print(number_list)

j = 0
for i in number_list:
    if i%2== 0:
        j=i+j
print(j)
