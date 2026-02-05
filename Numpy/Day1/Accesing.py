import numpy as np
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a)
print()

#get specific element
print(a[1][5])
print(a[1][-4])

print()

#spesific row
print(a[0,:])
print()

#specific column
print(a[:,2])
print()

#geting fancy [start index:end index:step index]
print(a[0,1:3:1])

#update element
a[1,5] = 34
print(a)

print()

#specific column element change 
a[:,5] = 5  
print(a)

print()

a[:,4] = [1,3]
print(a)


