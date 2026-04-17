from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import numpy as np

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,4,6,8,10])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

m = LinearRegression()

m.fit(x_train,y_train)

p = m.predict(x_test)

print("pred =",p)

print("score =",m.score(x_test,y_test))
