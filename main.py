import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('iris')
print(df.head())
sns.barplot(data=df,x='species',y='sepal_length')
plt.show()
sns.countplot(data=df,x='species')
plt.show()
sns.boxplot(data=df,x='species',y='sepal_width')
plt.show()
sns.swarmplot(data=df,x='species',y='sepal_width')
plt.show()