import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.set()
sns.set_style("darkgrid")

print(df.head())

sns.histplot(df["sepal_length"])
plt.show()

sns.kdeplot(df["sepal_width"])
plt.show()

sns.scatterplot(x="sepal_length",y="sepal_width",data=df)
plt.show()

sns.barplot(x="species",y="sepal_length",data=df)
plt.show()

g = sns.FacetGrid(df,col="species")
g.map(sns.scatterplot,"sepal_length","sepal_width")
plt.show()

sns.pairplot(df)
plt.show()
