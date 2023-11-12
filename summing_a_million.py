#Summing a Million, Making a list of the numbers from one to one million, 
#and then using min() and max() to make sure your list actually starts at one and 
#ends at one million. Also, using the sum() function to see how quickly Python can 
#add a million numbers.

#making a list of numbers from one to million
million = [mil for mil in range(1,1000001)]

#checking lowest number and highest number in the list
lowest = min(million)
highest = max(million)
print(lowest)
print(highest)

#total sum of the million number
sum_million = sum(million)
print(sum_million)
