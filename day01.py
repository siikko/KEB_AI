import numpy as np
import pandas as pd


#dataframe은 2차원의 표형태,serial은 1차원형태(예를들어, 열)
df = pd.DataFrame(
{"a" : [4, 5, 6],
      "b" : [7, 8, 9],
      "c" : [10, 11, 12]},
      index = [1, 2, 3]) #index:row명, dict의 key:column명
print(df)