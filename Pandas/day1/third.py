import pandas as pd

filedata = pd.read_csv('file.csv')
#summary _ function
print(filedata.ProductA.describe())

print()
print(filedata.ProductB.describe())

print()
print(filedata.ProductB.mean())

print()
print(filedata.ProductB.unique())

print()
print(filedata.ProductA.value_counts())

#Maps
map = filedata.ProductA.mean()
print(filedata.ProductA.map(lambda p:p - map))


def Product(row):
    row.ProductA = row.ProductA - map
    return row

print(filedata.apply(Product,axis = 'columns'))

print()
print(filedata.head(1))
print()
mean = filedata.ProductB.mean()
print(filedata.ProductB - mean)

print()
print()

print(f"{filedata.ProductA} ' - ' {filedata.ProductB}")