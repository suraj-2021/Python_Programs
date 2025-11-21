import numpy as np
n,m = map(int,input().split())
x = []
for _ in range(n):
    y = list(map(int,input().split()))
    x.append(y)
print(x)   
x = np.array(x)
print(x.flatten())
