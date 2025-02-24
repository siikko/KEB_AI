import pandas as pd
import matplotlib.pyplot as plt
import SElearn as se

ls=pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
X=ls[["GDP per capita (USD)"]].values
y=ls[["Life satisfaction"]].values
print(ls)
ls.plot(kind='scatter',grid=True,x="GDP per capita (USD)",
        y="Life satisfaction")#산점도를 그리겠다, 격자는 있어야하고 x와 y축은 해당 값들이 있어야 함.
plt.axis([23500,62500,4,9])#Matplotlib에서 그래프의 x축, y축의 범위를 설정하거나 숨기는 기능
plt.show()

model=se.KNeighborsRegressor()

model.fit(X,y)
X_new=[[37655.2]]
print(model.predict(X_new))

