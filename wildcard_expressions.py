import re
atRegex = re.compile(r'.at')
string = "lat apt hat cat chitchat mat"
mo = atRegex.findall(string)

for x in mo:
  print(x)
