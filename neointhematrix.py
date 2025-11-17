import re 
n,m = map(int,input().split())

arrays = []
for _ in range(n):
    arrays.append(list(input()))
word = ""
for i in range(m):  # columns
    for j in range(n):  # rows
        try:
            word += arrays[j][i]
        except IndexError:
            pass

pattern = r"(?<=\w)[^\w]+(?=\w)"

def replace(match):
    return " "
    
y = re.sub(pattern, replace, word)
print(y)
