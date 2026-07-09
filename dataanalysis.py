import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sns



# Arrays in Numpy
arr = np.array([[1,2,3],[4,5,6]])
print("Array: ", arr)
print("Shape:", arr.shape)
print("dimension:", arr.ndim)

#Creating Numpy Arrays
a = np.array([1,2,3])
b = np.zeros((2,2))
c = np.ones((2,2))
d = np.arange(0,10,2)
e = np.empty((2,2), dtype=int)
print(a)
print(b)
print(c)
print(d)
print(e)

# Analyzing data using pandas

data = [10,11,12,13,14]
series = pd.Series(data)
print(series)
print("first element: ", data[0])
print(series.ndim)


# DAta frame in Pandas
data = {
    'Name':['a','b','c'],
    'Age':[10,20,30]
}
df = pd.DataFrame(data)
print(df)
print(df['Name'])

# Pandas CRUD Operations
data = {
    'Name':['A','B','C'],
    'Age':[10,20,30]
}
# export to csv
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

# read csv file
df = pd.read_csv('data.csv')
print(df)

df['Age'] = df['Age'] + 1
df['City'] = ['JYU','Oulu','Vassa']

print("Updated: \n", df)

df.drop('City', axis=1, inplace=True)
print("AFter drop:\n", df)

df.drop(0, axis=0)
print("Delete :\n", df)


# Exploatory Data Analysis (EDA)

# 1. Data inspection
# info(), describe(), value_counts(), head(), tail()

data = {
    "Name": ["A", "B", "C", "A", "B"],
    "Age": [20, 21, 22, 20, 21]
}
df = pd.DataFrame(data)
print("INfo")
print(df.info())

print("Describe: \n", df.describe())
print("Value counts: \n", df['Name'].value_counts())

print("head: \n", df.head(2))
print("tails: \n", df.tail(3))

# 2. Data manipulation 
# indexing and selection
print(df['Name'])
print(df.loc[[1,2,3],'Name'])
print(df.iloc[2:5,1])

# Grouping and Aggrigation
print(df)
print(df.groupby('Name')['Age'].mean())

# Sort
print(df.sort_values(by='Age',ascending=False))


# Filter
print(df[df['Age'] > 20])
print(df[df['Age'] > 20]['Name'])

# set index
print(df.set_index('Name', inplace=True))
print(df)

#reset index
df.reset_index(inplace=True)
print(df)

# 3. Working with missing data
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [20, None, 22]
})
print(df)
print(df.isna())
print(df.isna().sum())

# dropping missing values
print(df.dropna())
print(df)

# fill null value
df['Age']=df['Age'].fillna(df['Age'].mean())
print(df)

# 4. Checking and handling duplicates values
df = pd.DataFrame({
    "Name": ["A", "B", "A", "C"],
    "Age": [20, 21, 20, 22]
})
print(df.duplicated())
print(df[df.duplicated()])
print(df.duplicated().sum())

# drop duplicated
df_clean = df.drop_duplicates()
print(df_clean)

#5. Outlier detection and handling
#IQR method
df = pd.DataFrame({
    "Values": [10, 12, 14, 15, 100]
})
q1 = df['Values'].quantile(0.25)
q3 = df['Values'].quantile(0.75)
IQR = q3 - q1 
outliers = df[(df['Values'] < q1 - 1.5 * IQR) | (df['Values'] > q3 + 1.5 * IQR)]
print("Q1:", q1)
print("Q3:", q3)

print("outliers: ", outliers)

# Z score method
df = pd.DataFrame({
    "Values": [10, 12, 14, 15, 100]
})
mean = np.mean(df['Values'])
std = np.std(df['Values'])
df['zscore'] = (df['Values'] - mean )/ std
print(df)

outliers = df[df['zscore'].abs() > 3]
print("Outliers: ", outliers)


# Data visualization using matplotlib

""" plt.plot([1,2,3,4],[1,4,9,16])
plt.axis([0,10,0,20])
plt.show() """

# bar chart
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.head())

counts = df['target'].value_counts()
print(counts)

""" plt.bar(counts.index, counts.values)
plt.title("Bar chart Iris dataset")
plt.xlabel("Index")
plt.ylabel("Count")
plt.show() """

# Histograms
""" 
plt.hist(df['sepal length (cm)'], bins=10)
plt.title("Histrogram iris dataset")
plt.xlabel("SEpal length")
plt.ylabel("Frequency")
plt.show() """

# Scatter plot
""" plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'])
plt.title("Scatter plot Iris dataset")
plt.ylabel('sepal width')
plt.xlabel('sepal lenght')
plt.show() """

# box plot
""" 
plt.boxplot(df['sepal width (cm)'], labels=['sepal width'])
plt.title("Box plot iris dataset")
plt.ylabel('Value')
plt.show() """

# correlation heatmaps
corr = df.corr()
print("correlation value: \n", corr)

""" plt.imshow(corr, cmap='autumn', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)),corr.columns)
plt.show() """

# data visualization using seaborn
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue="species", data=df)
plt.title("seaborn scatter plot")
plt.show()