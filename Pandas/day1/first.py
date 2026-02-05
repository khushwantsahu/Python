import pandas as pd

#creating DataFrame
dataframe1 = pd.DataFrame({'yes':[50,20],'no':[131,2]})
print(dataframe1)

dataframe2 = pd.DataFrame({'Bob':['i like it','it was hello'],'sue':['pretty good','bland']})
print(dataframe2)

dataframe3 = pd.DataFrame({'x':[11,22,33,44,55],'y':[11,22,33,44,55]})
print(dataframe3)

dataframe4 = pd.DataFrame({'bob':['i like it','not like it'],
                           'sue':['pretty good','bland']},
                           index=['product A','Product B'])
print(dataframe4)


#creating Series
series = pd.Series([1,2,3,4,5,6])
print(series)

series2 = pd.Series([1,2,3],index=['2015 sales','2016 sales','2017 sales'],name = 'product A')
print(series2)

review = pd.read_csv("file.csv")
print(review)

print(review.shape)
print(review.head())

review2 = pd.read_csv("file.csv",index_col = 0)
print(review2.head())

ingredients = pd.Series(['4 cups','1 cups','2 large','1 can'],index=['flour','milk','eggs','spam'],name= 'Dinner')

print(ingredients)