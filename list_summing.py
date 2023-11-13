#creating a program that sums the first 10 letters in the list
my_list = [i for i in range(1,10)]
total_sum = 0

for num in my_list:
    total_sum += num

print(f"The sum of the elements in the list is: {total_sum}")
