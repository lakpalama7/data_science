import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name':['a','b','c','d','e'],
    'age':[21,22,33,21,24]
}
df = pd.DataFrame(data)
print(df)

# Line plot
""" sns.lineplot(x=df.index, y='age', data=df)
plt.title("Age line plot")
plt.xlabel('index')
plt.ylabel("Age")
plt.show() """

# Scatter plot
""" sns.scatterplot(x='age',y=df.index, data=df)
plt.xlabel('age')
plt.ylabel('index')
plt.show() """

# boxplot
""" sns.boxplot(y='age', data=df)
plt.show() """

#violin plot
""" sns.violinplot(y='age', data=df)
plt.show() """

#bar plot
""" sns.barplot(x='Name',y='age',data=df)
plt.show() """

#count plot
""" data = {'Name': ['ANSH', 'SAHIL', 'ANSH', 'JAYAN', 'ANURAG', 'ANURAG', 'ANURAG', 'SAHIL']}
df = pd.DataFrame(data)
sns.countplot(x='Name',data=df)
plt.show() """

#kde plot
sns.kdeplot(x='age', data=df)
plt.show()