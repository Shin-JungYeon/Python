'''
Created on 2019. 7. 23.

@author: gd_4

pandasexcelex4.py : 모든 sheet 조회하기.
'''
import pandas as pd

infile = "sales_2013.xlsx"
outfile = "pandas_output4.xls"

dframe = pd.read_excel(infile, sheet_name=None, index_col=None)
row_output = []
for worksheet_name, data in dframe.items() :
#     row_output.append(data)  # 원본 엑셀 파일의 모든 내용을 저장.
    row_output.append(data[data["Sale Amount"].replace('$', '').replace(',', '').astype(float) > 2000.0])

# axis=0 : row 추가.
# axis=1 : column 추가.
filtered_row = pd.concat(row_output, axis=0, ignore_index=True)  # ignore_index=True : 인덱스 없앰

writer = pd.ExcelWriter(outfile)
filtered_row.to_excel(writer, sheet_name="sale_2013_gt2000", index=False)
writer.save()
