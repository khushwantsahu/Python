import numpy as np
'''
# 2. Print the numpy version and the configuration
print(np.__version__)
print(np.show_config())
'''

'''
# 3. Create a null vector of size 10 
vec = np.zeros(10,dtype='int32')
print(vec)
'''

'''
# 4. How to find the memory size of any array
arr = np.array((5,4))
print("%d bytes"%(arr.size*arr.itemsize))
print("%d bytes" %arr.nbytes)
'''

'''
# 5.Create a null vector of size 10 but the fifth value which is 1
vector = np.zeros(10)
vector[4] = 1
print(vector)
'''

'''
# 7. Create a vector with values ranging from 10 to 49
vector = np.arange(10,49)
print(vector)
'''

'''
# 8. Reverse a vector (first element becomes last)
arr = np.arange(10)
print(arr[::-1])
'''

'''
# 9. Create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(9)
matrix = matrix.reshape((3,3))
print(matrix)
'''

'''
# 10. Find indices of non-zero elements from [1,2,0,0,4,0]
arr = np.nonzero([1,2,0,0,4,0])
print(arr)
'''

'''
# 11. Create a 3x3 identity matrix 
arr = np.identity(3)
print(arr)
'''

'''
# 12. Create a 3x3x3 array with random values
random = np.random.random((3,3,3))
print(random)
'''

'''
# 13. Create a 10x10 array with random values and find the minimum and maximum values
arr = np.random.random((10,10))
print(arr)
print(f"minimum num = {arr.min()}")
print(f"maximum num = {arr.max()}")
'''

'''
# 14. Create a random vector of size 30 and find the mean value 
vector = np.random.random(30)
mean = vector.mean()
print(mean)
'''

'''
# 15. Create a 2d array with 1 on the border and 0 inside 
one = np.ones((4,4))
zero = np.zeros((2,2))
one[1:-1,1:-1] = zero
print(one)
'''

'''
# 16. How to add a border (filled with 0's) around an existing array?
array = np.ones((4,5))
#array[:,0],array[0,:],array[-1,:],array[:,-1] = 0 ,0,0,0
array[:,[0,-1]] = 0
array[[0,-1],:] = 0
print(array)
'''


'''
# 17. What is the result of the following expression
print(np.nan,np.inf)
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)
'''

'''
# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
'''

'''
# 19. Create a 8x8 matrix and fill it with a checkerboard pattern
array = np.zeros((8,8))
array[1::2,::2] = 1
array[::2,1::2] = 1
print(array)
'''


# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
print(np.unravel_index(99,(6,7,8)))





