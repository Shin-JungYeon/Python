'''
Created on 2019. 7. 23.

@author: gd_4

pandasexcelex1.py : pandas에서 excel 파일 읽기.
'''
import pandas as pd

infile = "sales_2013.xlsx"
outfile = "pandas_output.xls"
dframe = pd.read_excel(infile, "january_2013", index_col=None)
print(dframe)

# 행 선택 조건 : Sale Amount 컬럼의 값이 1400 초과인 행만 선택.
# dframe_value = dframe[dframe["Sale Amount"].astype(float) > 1400.0]  # Sale Amount 컬럼의 값을 float 형태로 바꾸고 1400 초과인 값들만 가져옴.

# 행 선택 조건 : Customer Name 컬럼의 값이 J 로 시작하는 행만 선택.
dframe_value = dframe[dframe["Customer Name"].str.startswith("J")]

writer = pd.ExcelWriter(outfile)  # xlwt 모듈 반드시 필요. 설치되어 있으면 pandas에서 알아서 가져옴.
dframe_value.to_excel(writer, sheet_name="jan_2013_outJ", index=False)
writer.save()