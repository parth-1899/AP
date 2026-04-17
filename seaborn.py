import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.set_style("darkgrid")

sns.histplot(df["sepal_length"],kde=True,color="purple")
plt.title("hist + kde")
plt.show()

sns.boxplot(x="species",y="sepal_length",data=df,palette="Set2")
plt.title("box plot")
plt.show()

sns.violinplot(x="species",y="sepal_width",data=df,palette="cool")
plt.title("violin plot")
plt.show()

sns.pairplot(df,hue="species")
plt.show()
