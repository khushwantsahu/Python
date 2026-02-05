import numpy as np

#load daa from file
data = np.genfromtxt("file.txt",delimiter=",")
print(data)
data = data.astype('int32')
print(data)

#advance indexing
#Boolean masking 

print(data > 50)
print(data >= 50)
print()
print(data[data>50])

print(data[data<40])

#index with a list in numpy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,7]])

print(a[[5,6]])

print(np.any(data > 50,axis=0))
print(np.all(data > 50,axis=0))
print()

print((data>50)*(data <100))
print(data[(data > 50)  & (data < 100)])

print(~((data>50)*(data <100)))




