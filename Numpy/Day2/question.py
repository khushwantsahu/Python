import numpy as np
#que:-
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1

a = np.ones((5,5))
print(a)

print()

zero = np.zeros((3,3))
zero[1,1] = 9
print(zero)
print()


#a[1:4,1:4]  = zero
a[1:-1,1:-1]  = zero
print(a)




