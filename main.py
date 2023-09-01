import pandas as pd
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

print(df.count())

grouped_by_tag = df.groupby("TAG")
print(grouped_by_tag["POSTS"].sum())


print(df["DATE"][1]) #second entry in the DATE column, and it's a string.
print(pd.to_datetime(df["DATE"][1])) #second entry in the DATE column, and it's a pandas object.

df.DATE = pd.to_datetime(df.DATE) #convert the entire column from strings to pandas objects.
