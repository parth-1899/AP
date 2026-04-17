import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(x,y,label="line")
plt.title("line graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()

plt.bar(x,y)
plt.title("bar graph")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.scatter(x,y)
plt.title("scatter")
plt.show()

plt.hist(y)
plt.title("hist")
plt.show()

l = ["a","b","c","d"]
v = [20,30,25,25]

plt.pie(v,labels=l,autopct="%1.1f%%")
plt.title("pie")
plt.show()
