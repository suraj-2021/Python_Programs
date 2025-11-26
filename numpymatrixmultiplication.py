import numpy as np
n = int(input()) 
a1 = []
b1 = [] 

for _ in range(n):
    a1.append(list(map(int,input().split())))
for _ in range(n):
    b1.append(list(map(int,input().split()))) 
    
a = np.array(a1)
b = np.array(b1) 

print(np.matmul(a,b))
