#Reading the whole text file an printing the contents line by line.
filename = 'digits.txt'
with open(filename) as file_object:
lines = file_object.readlines()
for line in lines:
      print(line.rstrip())
