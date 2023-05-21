import numpy as np
#ohne numpy
def transform_nobranch(x):
 list = []
 for y in x:
    list.append(int(y<0.5)* (2*y-1)+ int(y>= 0.5)*round((3*y+0.5)))
 return list

#mit numpy
def transform_nobranch(x):
 return np.where(x < 0.5, 2*x - 1, np.round(3*x + 0.5))
