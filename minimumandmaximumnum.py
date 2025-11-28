import numpy as np 
n,m=map(int,input().split()) 
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split()))) 
my_arr = np.array(arr)
x=np.min(my_arr,axis = 1)
print(np.max(x))
