import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# load dataset
df = pd.read_csv('covid.csv')
print(df.head())

# return rows and columns
print(df.shape)

# return size of datafram
print(df.size)

# info
print(df.info())

# import dataset 2
df1=pd.read_csv('covid_grouped.csv')
print(df1.head())

print(df1.shape)
print(df1.size)
print(df1.info())

# data cleaning

print(df.columns)
print(df.isna().sum())

#We don't need 'NewCases', 'NewDeaths', 'NewRecovered' columns as they contains NaN values. So drop these columns by drop() function of pandas.
df.drop(['NewCases','NewDeaths','NewRecovered'], inplace=True, axis=1)
print(df.isna().sum())

# bar graph
""" sns.barplot(x='Country/Region', y='TotalCases',color='red', data=df.head(15))
plt.show() """

""" sns.barplot(x='TotalTests',y='Country/Region', data=df.head(15))
plt.show() """

# Bubble chart
""" sns.scatterplot(x='Continent', y='TotalCases', data=df)
plt.show() """

""" sns.scatterplot(x='Country/Region', y='TotalCases', data=df, size='TotalCases')
plt.show() """

# Country specific data visualization. US
df_us = df1[df1['Country/Region']=='US']
print(df_us.head())

# Bar char
""" sns.barplot(x='Date', y='Confirmed', data=df_us)
plt.show() """

# LIne plot
""" sns.lineplot(x='Date',y='Recovered', data=df_us)
plt.show() """

""" sns.lineplot(x='Date', y='New cases', data=df_us)
plt.show() """
""" sns.barplot(x='Date', y='New cases', data=df_us)
plt.show() """

# scatter plot
sns.scatterplot(x='Confirmed',y='Deaths', data=df_us)
plt.show()