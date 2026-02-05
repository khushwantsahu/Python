import numpy as np

a = np.array([[[1,2,3],[1,2,3]],[[4,5,6],[4,5,6]]])
print(a)
print()
#replace
a[:,1,:] = [[1,2,1],[12,12,23]]
print(a)

print()
#all 0s element matrix
print(np.zeros((2,3)))

print()

#all 1s matrix
print(np.ones((4,2,2),dtype='int32'))

#any number
b = np.full((2,3),99,dtype='float32')
print(b.dtype)

#any other number(full_like)
#c = np.full_like(a,4)
c = np.full(a.shape,4)

print(c)

#randome decimal number
#d = np.random.rand(4,2,4)
d = np.random.random_sample(a.shape)
print(d)

#randome integer value
e = np.random.randint(0,1,size=(4,4))
print(e)

#the identity number
f = np.identity(3)
print(f)

print()

#repeat an array
arr = np.array([[1,2,3]])
arr1 = np.repeat(arr,2,axis=0)
print(arr1)
