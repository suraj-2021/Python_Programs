import re

s = 'GITHUB GITHUB: A computer science portal for geeks'
match = re.search(r'portal', s)

if match:
    print('Start Index:', match.start())
    print('End Index:', match.end())
else:
    print('Pattern not found.')
