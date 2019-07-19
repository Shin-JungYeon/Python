'''
Created on 2019. 7. 19.

@author: gd_4

pandasex2.py
'''
import pandas as pd
input_file = "supplier_data.csv"
output_file = "pandas_out2.csv"

data_frame = pd.read_csv(input_file)
'''
    row 선택 기준 설정 명령어.
        loc : Header 값으로 선택.
        iloc : 숫자 인덱스로 선택.
        ix : 둘 다 가능.
'''
data_frame_in_set = \
    data_frame.loc[data_frame["Invoice Number"].str.startswith("001-")]  # 열에 대한 정보가 없으므로 모든 열을 가져옴.
print(data_frame_in_set)

data_frame_in_set.to_csv(output_file, index=False)