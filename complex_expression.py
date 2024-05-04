import re
xRegex = re.compile(r'\d+\s\w+')
mo = xRegex.fidall("12 south, 13 west,16 north, 18 east")

print(mo.group())
