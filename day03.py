import pandas as pd

data=[1,7,5,2,8,3,6,4]
bins=[0,3,6,9] #구간을 0~3,3~6,6~9로 3개씩 나눔
labels=["low","mid","high"] #위의 각 구간의 이름은 low, mid, high

cat=pd.cut(data,bins,True,labels)
print(cat)