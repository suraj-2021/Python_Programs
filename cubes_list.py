# Making a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and printing out the list.


#creating a empty list
cubes= []

#using a for loop and range function  to access integers ranging from 1 to 10
for i in range(1,11):
    i = i**3
    cubes.append(i)

#printing the final list
print(cubes)
