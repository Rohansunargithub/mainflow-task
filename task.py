import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('housing_dataset.csv')
df.head()
df.info()
df.describe()
df.isnull().sum()
df = df.dropna() 
df.hist(bins=15, figsize=(15,10))
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.show()
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
sns.pairplot(df)
plt.show()
sns.boxplot(x=df['rohan'])
plt.show()

Q1 = df['rohan'].quantile(0.25)
Q3 = df['rohan'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['rohan'] < (Q1 - 1.5 * IQR)) | (df['rohan'] > (Q3 + 1.5 * IQR))]
print(outliers)

