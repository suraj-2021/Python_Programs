import re 
decca = re.compile(r'(.*)', re.DOTALL)
data = """ First Name: Suneel \n Last Name: Khera"""

mo = decca.findall(data)

attypes = []
for i in mo:
    attypes.append(i)
print(attypes)
