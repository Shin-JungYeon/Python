'''
Created on 2019. 7. 19.

@author: gd_4

pandasex1.py
'''
import pandas as pd  # pip3 install pandas
input_file = "supplier_data.csv"  # 원본 데이터.
output_file = "pandas_out1.csv"

data_frame = pd.read_csv(input_file)  # input_file에 저장된 문자열과 같은 이름을 가진 csv 파일을 읽어와서 데이터를 표로 저장. 첫 줄은 header.
print(data_frame)
print(type(data_frame))  # 'pandas.core.frame.DataFrame'
dates = ["1/20/14", "1/30/14"]

data_frame_in_set = \
    data_frame.loc[data_frame["Purchase Date"].isin(dates),:]  # loc : 행과 열의 2차원 배열로 표시. , 를 기준으로 앞이 행(Purchase Date 이름의 열에서 dates인 행들만 선택), 뒤가 열(:은 전부를 의미).
data_frame_in_set.to_csv(output_file, index=False)
