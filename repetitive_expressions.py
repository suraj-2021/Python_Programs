import re

mayRegex = re.compile(r'(Ma){5}')

mo = mayRegex.search('MaMaMaMaMa')

print(mo.group())
