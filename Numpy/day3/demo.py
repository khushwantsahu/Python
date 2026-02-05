import numpy as np


n = np.array([[1,2,3,4,5],[1,2,3,4,4]])
'''
print(n+1)
print(n-1)
print(n*1)
print(n**2)
print(n/1)
print(n//2)

print(np.sqrt(n))
print(np.mean(n))
print(np.max(n))
print(np.min(n))
print(np.log(n))
print(np.exp(n))


print(n.sum(axis=0,keepdims= True))
print(n.argmax(axis=1))
print(n.std())
print(n.var())
print(n.sum(axis=1).mean())

print(n.shape)
print(n.reshape(5,2))
print(n.flatten())
print()
print(n.ravel())
print(n.T)
'''
b1 = np.ones((2,5))

print(b1 is n )

#print(n @ b)
#s  = np.dot(n, b1)
#print(n@b1)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

s= np.dot(a,b)
s = a @ b
print(s)

mean = a.mean()
std = a.std()
ans = (a-mean)/std
print(ans)

