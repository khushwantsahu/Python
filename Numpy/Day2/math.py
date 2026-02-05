import numpy as np
#Be Carefull copy an arrau
print()
b = np.array([1,2,3,4])
#c = b  # it give same address of the b
c = b.copy()
c[0] = 100
print(b)
print(c)

print()

#math
print(b+2)

print("\n", b-2)

print("\n",b*3)

print("\n",b/2)

a = np.array([1,3,5,6])
c = a+b
print(c)

print("\n",a**2)

print("\n",np.sin(a))

print("\n",np.cos(a))

print("\n",np.tan(a))


