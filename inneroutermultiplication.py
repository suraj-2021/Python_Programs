import numpy as np
ar = np.array([list(map(int,input().split())) for _ in range(2)])
print(np.inner(ar[0],ar[1]))
print(np.outer(ar[0],ar[1]))
