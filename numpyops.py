import numpy as np
np.set_printoptions(legacy='1.13')
a = list(map(float,input().split()))
ar = np.array(a)
print(np.floor(ar))
print(np.ceil(ar)) 
print(np.rint(ar))
