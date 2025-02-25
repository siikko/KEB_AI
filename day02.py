#결측치값을 산술평균으로 채워 넣기
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df=pd.DataFrame({

    'A':[1,2,np.nan,4],
    'B':[np.nan,12,3,4],
    'C':[1,2,3,4]
})
print(df)

# df_option=df.copy()
# mean_value=df_option.mean()
# df_option.fillna(mean_value,inplace=True)
# print(df)

i=SimpleImputer(strategy='mean')
df[['A','B']]=i.fit_transform(df[['A','B']])
print(df)