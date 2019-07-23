'''
Created on 2019. 7. 23.

@author: gd_4

pandasexcelex3.py : excel 파일을 읽어서 컬럼들만 선택하기.
'''
import pandas as pd

infile = "sales_2013.xlsx"
outfile = "pandas_output3.xls"

dframe = pd.read_excel(infile, "january_2013", index_col=None)
# dframe_value = dframe.loc[:, ["Customer Name", "Purchase Date"]]  # 컬럼명으로 선택
dframe_value = dframe.iloc[:, [1, 4]]  # 컬럼 번호로 선택.

writer = pd.ExcelWriter(outfile)
dframe_value.to_excel(writer, sheet_name="jan_2013_col", index=False)
writer.save()