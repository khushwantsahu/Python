import numpy as np

a = np.array([1,2,3])
print(a)

b = np.array([[12,23,23,35],[3,55,34,12]])
print(b)

#get diamention
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)
print()

#Get Type
print(a.dtype)

#we can specify the data type
c =  np.array([1,2,3],dtype='int32')
print(c.dtype)

#Get size
print(a.itemsize)

#total size
print(a.size)
print(b.size)
print()
print(a.itemsize)
print(b.itemsize)

