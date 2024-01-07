#Opening the file and reading it/printing the content.
with open('pi_digits.txt') as file_object:
 contents = file_object.read()
print(contents)
