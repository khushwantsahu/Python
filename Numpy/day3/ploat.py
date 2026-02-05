import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5]
y = [10,12,33,35,55]



'''
plt.xlabel("x value")
plt.ylabel("y value")
plt.title("Simple Line Plot")
plt.plot(x,y)
plt.show()


y2 = [2,35,3,4,5]

plt.plot(x,y,label="line 1")
plt.plot(x,y2,label="label 2")
plt.legend()
plt.show()


plt.xlabel("x")
plt.ylabel("y")
plt.title("scatter")
plt.scatter(x,y)
plt.show()

cat = ["a","b","c"]
val = [10,12,23]
plt.bar(cat,val)
plt.title("barchart")
plt.show()

data = [1,2,1,1,2,2,2,3,4,5,5,3,3,4,4,4]
plt.hist(data)
plt.title("histogram")
plt.show()

x = np.linspace(0,10,100)
y = np.sin(x)
print(x)
plt.plot(x,y)
plt.show()'''

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr1 = np.ones((3,4))
np.savetxt('array.txt', arr, fmt='%d')

# Load from text
loaded_txt = np.loadtxt('array.txt', dtype=int)
print(loaded_txt)

data = np.genfromtxt("array.txt",dtype='int')
print(data)

np.savetxt("arr.csv",arr1,fmt="%d")
data = np.loadtxt("arr.csv",dtype="int")
print(data)
