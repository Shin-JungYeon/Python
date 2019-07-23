'''
Created on 2019. 7. 23.

@author: gd_4

pandasexcelex5.py : 모든 sheet 조회하여 조건에 맞는 컬럼 선택하기.
'''
import pandas as pd

infile = "sales_2013.xlsx"
outfile = "pandas_output5.xls"

dframe = pd.read_excel(infile, sheet_name=None, index_col=None)
col_output = []

for worksheet_name, data in dframe.items() :
    col_output.append(data.loc[:, ["Customer Name", "Sale Amount"]])

select_cols = pd.concat(col_output, axis=1, ignore_index=False)  # ignore_index=False : 원본의 컬럼명 그대로 가져옴.
writer = pd.ExcelWriter(outfile)
select_cols.to_excel(writer, sheet_name="sale_2013_cols", index=False)
writer.save()