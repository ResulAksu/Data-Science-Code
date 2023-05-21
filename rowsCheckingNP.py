import numpy as np
def has_zero_rows(M):
    if np.any(np.sum(M,axis=1) == 0):
        return True
    return False

# alle max werte mit maske 
a = np.genfromtxt('iris_toy.csv', delimiter=',',
skip_header=1, usecols=(0,1,2,3), dtype=np.float64)
print(a[np.any(np.logical_or(a == a.max(axis=0), (a != a)), axis=1)])