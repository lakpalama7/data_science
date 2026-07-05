import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load data
df = pd.read_csv('airbnbdata.csv')
print(df.head())

print(df.columns)

# missing values
print(df.isna().sum())
# dataset structure
print(df.info())

# convet 'last review' to datetime and handle errors
df['last review'] = pd.to_datetime(df['last review'], errors='coerce')
print(df.info())

# fill missing values
df.fillna({'reviews per month':0, 'last review':df['last review'].min()}, inplace=True)

# drop records with missing 'name' or 'host name'
df.dropna(subset=['NAME','host name'], inplace=True)
print(df.isna().sum())

# Correct data types
print(df[['price','service fee']].head())
# remove dollor sign and convert to float
df['price'] = df['price'].replace('[\$,]','', regex=True).astype(float)
df['service fee'] = df['service fee'].replace('[\$,]','',regex=True).astype(float)
print(df[['price','service fee']].head())

# Remove duplicates
print(df.info())
df.drop_duplicates(inplace=True)
print(df.info())

# descriptive statistics
print(df.describe())

#visualization: distribution of price
""" plt.figure(figsize=(10,6))
sns.histplot(x=df['price'], bins=50, kde=True)
plt.title("Distribution of listing price")
plt.xlabel("price")
plt.ylabel("frequency")
plt.show() """
# histogram shows fairly even distribution of prices


#Room type analysis
""" plt.figure(figsize=(10,6))
sns.countplot(x=df['room type'], data=df, color='hotpink')
plt.title("Room type distribution")
plt.xlabel("Room Type")
plt.ylabel("count")
plt.show() """
# the countplot show The majority of listings are for 'Entire home/apt' and 'Private room',


# Neighborhood analysis
""" plt.figure(figsize=(10,6))
sns.countplot(y=df['neighbourhood group'], data=df, color='lightgreen', order=df['neighbourhood group'].value_counts().index)
plt.title("Listing by neighbourhood group")
plt.ylabel("Neighbourhood group")
plt.xlabel("Count")
plt.show() """

#countplot shows Manhattan and Brooklyn dominate the listings, suggesting they are prime locations for Airbnb.

# price vs room type
""" plt.figure(figsize=(10,6))
sns.boxplot(x='room type', y='price', hue='room type', data=df, )
plt.title("Price vs room type")
plt.xlabel('room type')
plt.ylabel('price')
plt.legend()
plt.show() """

# boxplot shows t shows that while 'Shared room' tends to have lower prices, 'Private room', 'Entire home/apt', and 'Hotel room' have higher and more varied price ranges. 


# REview over time
review = df.groupby(df['last review'].dt.to_period('M')).size()
plt.figure(figsize=(10,6))
review.plot(kind='line',color='red')
plt.title("REview over time")
plt.xlabel("date")
plt.ylabel("No of review")
plt.show()
#The line plot provides a clear visualization of the number of reviews over time. 
