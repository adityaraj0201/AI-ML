import numpy as np
#matrix multiplication
a=np.array([[1,2],[3,4]])
b=np.array([[7,8],[5,6]])
c=np.dot(a,b)
print(c)
#matrix sumission
print(a+b)
#finding max and min values of c
print("max value ", np.max(c))
print("min value ", np.min(c))
print("max value along axis 0", np.max(c,axis=0))
print("max value along axis 1 ", np.max(c,axis=1))