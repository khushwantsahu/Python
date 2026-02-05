import pandas as pd
'''
#read from csv file
filedata = pd.read_csv('file.csv',index_col = 0)

filedata = pd.read_csv('file.csv')

#print(pd.set_option('display.max_rows',2))

print(filedata)
print(filedata.ProductB)
print()
print(filedata['ProductB'])

print()
print(filedata['ProductB'][0])


#index based selection
print()
print(filedata.iloc[0])

print()
print(filedata.iloc[1])

print()
print(filedata.iloc[2])

print()
print(filedata.iloc[:,1])

print()
print(filedata.iloc[:2,0])

print()
print(filedata.iloc[1:3,1])

print()
print(filedata.iloc[[0,1,2],2])

print()
print(filedata.iloc[-2])

#label based selection 
print(filedata.loc[1,'ProductA'])

print()
print(filedata.loc[1:2,['ProductA','ProductB','ProductC']])



#Manipulating the index
print()
print(filedata.set_index("ProductC"))

print()
print(filedata.ProductA == 35)

print()
print(filedata.loc[filedata.ProductC == 1])

print()
print(filedata.loc[filedata.ProductA.notnull()])

print()
print(filedata.loc[filedata.ProductA.isin([34,35])])

print()
print(filedata.loc[(filedata.ProductA == 30) | (filedata.ProductC >= 1)])

print()
print(filedata.loc[(filedata.ProductA == 30) & (filedata.ProductC >= 1)])


#Assigning data
filedata['ProductA'] = 'he'
print(filedata['ProductA']) #column value now is he

print()
filedata['ProductC'] = range(len(filedata),0,-1)
print(filedata['ProductC'])
'''

#write on csv file
data = pd.DataFrame({'A':[1,2,3,4,5],'B':[6,7,8,9,10],'C':[11,12,13,14,15]})
data.to_csv('file1.csv',mode = 'a',index = 0)


