'''
Created on 2019. 7. 23.

@author: gd_4

pandasexcelex2.py : "sales_2013.xlsx" 파일을 읽어서 Puarchase Date 컬럼의 값이 
    2013-01-24, 2013-01-31 인 행만 조회하여 pandas_out2.xls 파일의 "jan_2013_2431" sheet에 저장하기.
'''
import pandas as pd

infile = "sales_2013.xlsx"
outfile = "pandas_output2.xls"
dframe = pd.read_excel(infile, "january_2013", index_col=None)
print(dframe)

selectDate = ["2013-01-24", "2013-01-31"]
dframe_value = dframe[dframe["Purchase Date"].isin(selectDate)]

writer = pd.ExcelWriter(outfile)  # xlwt 모듈 반드시 필요. 설치되어 있으면 pandas에서 알아서 가져옴.
dframe_value.to_excel(writer, sheet_name="jan_2013_2431", index=False)
writer.save()
