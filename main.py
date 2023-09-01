import pandas as pd
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

print(df.count())

grouped_by_tag = df.groupby("TAG")
print(grouped_by_tag["POSTS"].sum())


