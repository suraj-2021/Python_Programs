import re
firstlast = re.compile(r"First Name: (.*)")
data = "First Name: Kartik"

mo = firstlast.search(data)

print(mo.group(1)
