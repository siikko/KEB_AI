#나이(X)에 따른 생존률 (y)
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


titanic=sns.load_dataset('titanic')
print(type(titanic)) #<class 'pandas.core.frame.DataFrame'>
print(titanic.info())
print(titanic.head())
titanic = titanic.dropna(subset=["age"])
x_train=titanic[["age"]].values #x_train데이터 추출
y_train=titanic["survived"].values #y_train데이터 추출

titanic.plot(kind='scatter',grid=True,x="age",
        y="survived")
plt.show()

model=KNeighborsClassifier()
model.fit(x_train,y_train)
x_test=np.array([[25]])
print(model.predict(x_test))