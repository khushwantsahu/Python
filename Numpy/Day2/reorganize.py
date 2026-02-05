import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

#show the matrix m*n
print(arr.shape)

#dimension
print(arr.ndim)

#reshape
#after = arr.reshape((4,2))
after = arr.reshape((2,2,2))
print(after)

