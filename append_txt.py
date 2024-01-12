# Program to append to a text file
with open('file1.txt', 'a') as f:
    f.write('\nHello again, World!')
print("Text has been appended to file1.txt")
