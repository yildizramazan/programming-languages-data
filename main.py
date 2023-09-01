import pandas as pd
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

print(df.count())
# DATE     1991
# TAG      1991
# POSTS    1991
# dtype: int64

grouped_by_tag = df.groupby("TAG")
print(grouped_by_tag["POSTS"].sum())
# TAG
# assembly        34852
# c              336042
# c#            1423530
# c++            684210
# delphi          46212
# go              47499
# java          1696403
# javascript    2056510
# perl            65286
# php           1361988
# python        1496210
# r              356799
# ruby           214582
# swift          273055
# Name: POSTS, dtype: int64

print(type(df["DATE"][1])) #second entry in the DATE column, and it's a string.
#<class 'str'>

print(type(pd.to_datetime(df["DATE"][1]))) #second entry in the DATE column, and it's a pandas object.
#<class 'pandas._libs.tslibs.timestamps.Timestamp'>

df.DATE = pd.to_datetime(df.DATE) #convert the entire column from strings to pandas objects.


#Data Manipulation: Pivoting DataFrames
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
print(test_df)
#      Age      Actor  Power
# 0  Young       Jack    100
# 1  Young     Arnold     80
# 2  Young      Keanu     25
# 3  Young  Sylvester     50
# 4    Old       Jack     99
# 5    Old     Arnold     75
# 6    Old      Keanu      5
# 7    Old  Sylvester     30


#.pivot() method
pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power') #The index is the categories for the rows. The columns are the categories for the columns. And the values are what you want in the new cells.
print(pivoted_df)
# Actor  Arnold  Jack  Keanu  Sylvester
# Age
# Old        75    99      5         30
# Young      80   100     25         50




reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")

print(reshaped_df.shape)
#(145, 14)

print(reshaped_df.columns)
# Index(['assembly', 'c', 'c#', 'c++', 'delphi', 'go', 'java', 'javascript',
#        'perl', 'php', 'python', 'r', 'ruby', 'swift'],
#       dtype='object', name='TAG')

print(reshaped_df.head())
# TAG         assembly      c      c#    c++  ...  python    r   ruby  swift
# DATE                                        ...
# 2008-07-01       NaN    NaN     3.0    NaN  ...     NaN  NaN    NaN    NaN
# 2008-08-01       8.0   85.0   511.0  164.0  ...   124.0  NaN   73.0    NaN
# 2008-09-01      28.0  321.0  1649.0  755.0  ...   542.0  6.0  290.0    NaN
# 2008-10-01      15.0  303.0  1989.0  811.0  ...   510.0  NaN  249.0    NaN
# 2008-11-01      17.0  259.0  1730.0  735.0  ...   452.0  1.0  160.0    NaN
#
# [5 rows x 14 columns]

print(reshaped_df.count())
# TAG
# assembly      144
# c             144
# c#            145
# c++           144
# delphi        144
# go            129
# java          144
# javascript    144
# perl          144
# php           144
# python        144
# r             142
# ruby          144
# swift         135
# dtype: int64


#Dealing with NaN Values ( .fillna() )
reshaped_df.fillna(0, inplace=True)  #first argument (which is 0 in this piece of code) is what you want to substitute for each NaN value and the inplace determines whether if the DateFrame is going to be updated.

##################################
#Data Visualisation with Matplotlib
import matplotlib.pyplot as plt
plt.figure(figsize=(16,10)) #allows us to resize our chart
plt.xticks(fontsize=14) #configures our x-axis
plt.yticks(fontsize=14) #configures our y-axis
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], label=reshaped_df[column].name)
plt.legend(fontsize=16)
plt.show()
