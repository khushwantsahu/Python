import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[11,12],[7,8],[14,24]])

c = np.ones((2,3))
d = np.full((3,2),5)

print(f"{a}\n\n{b}\n\n{c}\n\n{d}\n")

print(np.matmul(a,b))
print()

#find the determinant
e = np.identity(1)
print(np.linalg.det(e))

f = np.identity(6)
print(f)

