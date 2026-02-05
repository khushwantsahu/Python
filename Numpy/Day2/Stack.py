import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,1,4,2])


print(np.vstack([a,b,b,a]))
print()

#horizontal Stack
print(np.hstack([a,b]))