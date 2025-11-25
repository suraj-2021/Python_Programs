import numpy as np
n,m = map(int,input().split()) 

arr = []
for _ in range(n):
   arr.append(list(map(int,input().split()))) 
a = np.array(arr) 
x = np.sum(a,axis=0)
print(np.prod(x))
