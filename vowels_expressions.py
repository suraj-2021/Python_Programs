import re

cuRegex = re.compile(r'[aeiouAEIOU]')

print (cuRegex.findall('The, quick, brown, fox, jumps, over, the, lazy, dog'))

