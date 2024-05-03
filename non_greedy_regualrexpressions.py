import re

mayRegex = re.compile(r'(Ha){3,5}?')

mo = mayRegex.search('HaHaHaHaHa')

print(mo.group())
