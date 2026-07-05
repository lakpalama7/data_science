import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load data
df = pd.read_csv('ipldataset.csv')
print(df.head())

# drop 'unnamed: 0' column
df.drop('Unnamed: 0', inplace=True, axis=1)
print(df.head())
print(df.info())

# most expensive players
ex_df=df['Cost IN $ (000)'].max()
print("High $ cost: ", ex_df)
# get player name expensive
player_name = df.loc[df['Cost IN $ (000)']==ex_df,"Player's List"]
print(player_name)

x= df.groupby('Cost IN $ (000)')["Player's List"].count().tail(3)
print(x.index)

name=[]
for index, row in df.iterrows():
    for i in x.index: 
        if row['Cost IN $ (000)'] == i:
            name.append(row["Player's List"])

print(f"Top 3 most expensive palyers: ", name)