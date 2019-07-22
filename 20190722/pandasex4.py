'''
Created on 2019. 7. 22.

@author: gd_4

pandasex4.py
'''
import pandas as pd
df = pd.DataFrame(data=([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                        index=[2, "A", 4], columns=[51, 52, 53])  # index : 행의 이름들. columns : 열의 이름들.
print(df)  # 표로 만들어 줌.
print(df.iloc[2])  # 세 번 째 행. 이름과 상관 없이 2번째 행 가져옴(0부터 시작).
# print(df.iloc[2])  # error. 4번 째 행은 없음.
print(df.loc[2])  # 첫 번 째 행. 2라는 이름을 가진 행의 값들을 가져옴.
print(df.loc[4])  # 행의 이름이 4인 행. -> 세 번 째 행.
print(df.loc['A'])  # 행 중에 A라는 이름을 가진 행들 가져옴.

df = pd.read_csv("supplier_data.csv")  # csv 파일 pandas로 바로 읽을 수 있음.
print(df)
dcol = df.iloc[:, 1:3]  # [:(모든행), 1:3(1열부터 3열 앞까지)]
print(dcol)
