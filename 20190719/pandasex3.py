'''
Created on 2019. 7. 19.

@author: gd_4

pandasex3.py
'''
import pandas as pd
df = pd.DataFrame({"A":[1, 4, 7], "B":[2, 5, 8], "C":[3, 6, 9]})  # dictionary를 pandas 형태의 데이터로 생성 가능. A열의 행들, B열의 행들..
print(df)
print(df.loc[0])  # 행 선택 기준. 이름으로 가져옴.
print(df.iloc[0])  # 0 번 째 인덱스 가져옴.
# print(df.ix[0])