import numpy as np
n,m,p = map(int,input().split())

a1 = []
a2 = [] 

for _ in range(n):
    x = list(map(int,input().split()))
    a1.append(x) 
    
for _ in range(m):
    x = list(map(int,input().split()))
    a2.append(x)  

npa1 = np.array(a1)
npa2 = np.array(a2) 

output = np.concatenate((npa1,npa2),axis=0)
print(output)
