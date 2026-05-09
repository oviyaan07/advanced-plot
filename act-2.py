import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset('tips')
print(df.head())
sns.histplot(df['total_bill'],kde=True)
plt.show()
sns.scatterplot(data=df,x='total_bill',y='tip',hue='time')
plt.show()