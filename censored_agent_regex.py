import re
myRegex = re.compile(r'film \w+')

am = myRegex.sub('CENCER', 'The on python programming cannot be transtaled as a film. To be a film it will to be more emotional then technical. These books are ment to educate one about the programming rather them making a film. If you want to make a film you might want to choose novels, stories , biographies but technical book will not give you stories to make a film')

print(am)
