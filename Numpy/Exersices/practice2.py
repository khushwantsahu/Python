import numpy as np

arr = np.array([[1,2,3],[1,2,3]])
'''empty = np.empty((2,3))
sequance  = np.arange(1,50,2)
arr = np.linspace(0,5,5)
arr = np.random.rand(2,3)
arr = np.random.randn(2,3)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.reshape(3,2))
'''
'''
print(arr[2:6:2])
print(arr[::2])
print(arr[1])
print(arr[:3])
print(arr[::-1])

print(arr[arr > 2])'''
a = np.array([[1,2,3],[1,2,3]])
#print(arr+a)
print(a.mean(axis=0))