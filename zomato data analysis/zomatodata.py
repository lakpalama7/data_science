import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load data

df = pd.read_csv("zomatodata.csv")
print(df.head())

# data cleaning and preparation
# convert rate column to float and remove the denominator

def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

df['rate'] = df['rate'].apply(handleRate)
print(df['rate'])

# summary of dataset
print(df.info())

# check missing or null values
print(df.isna().sum())

# Exploring restaurant type
""" sns.countplot(x=df['listed_in(type)'])
plt.xlabel("type of restaurant")
plt.show() """

# majority of restaurant fall into dining category

# votes by restaurant type
# get vote count for each category
""" group_data = df.groupby('listed_in(type)')['votes'].sum()
print(group_data)
result = pd.DataFrame({'votes':group_data})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of restaurant')
plt.ylabel('votes')
plt.show() """
# dinning restaurant are prefered by larger number of individuals

# Idenfity the most voted restaurant
max_vote = df['votes'].max()
print(f"Max vote: ", max_vote)
rest_name = df.loc[df['votes'] == max_vote, 'name']
print(f"Restaurant name with max vote is : ", rest_name)

# Online order availability
# Explore how many restaurant accept online orders
""" sns.countplot(x=df['online_order'])
plt.show() """

#Conclusion: majority of restaurant do not accept online order

# Analyze Ratings
""" plt.hist(df['rate'], bins=5)
plt.title("Rating distribution")
plt.show() """
#Conclusion: Majority received rating between 3.5 to 4

# Approximate cost for couples
""" couple_data = df['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show() """
# conclusion: Majority couples prefer restaurant with cost of 300

# Rating comparision - online vs offline order
""" plt.figure(figsize=(6,6))
sns.boxplot(df, x='online_order', y='rate')
plt.show() """

# conclusion : Online order received more rating than offline order

# Order mode preferences by restaurant type
pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title("heatmap")
plt.xlabel('online order')
plt.ylabel('restaurant type')
plt.show()

# Conclusion: Dinning restaurant accept offline orders most, whereas cafes receive online order most