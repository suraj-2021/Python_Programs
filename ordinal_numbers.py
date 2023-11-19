#Store the numbers 1 through 9 in a list.
#Loop through the list.
#Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 
#7th 8th 9th", and each result should be on a separate line

list = [i for i in range(1,10)]

for i in list:
    if i == 1:
       print(f"{i}st")
    elif i ==2:
         print(f"{i}nd")
    elif i ==3:
         print(f"{i}rd")
    elif i ==4:
         print(f"{i}th")
    elif i ==5:
         print(f"{i}th")
    elif i ==6:
         print(f"{i}th")
    elif i ==7:
         print(f"{i}th")
    elif i ==8:
         print(f"{i}th")
    elif i ==9:
         print(f"{i}th")
