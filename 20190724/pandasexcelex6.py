'''
Created on 2019. 7. 24.

@author: gd_4

pandasexcelex6.py : 폴더의 모든 엑셀(xlsx, xls) 파일을 읽어서 pandas 데이터 생성하기.
'''
# D:\Python\eclipse-workspace-Python\pythontest\excelfile
import pandas as pd
import glob
import os  # 기본 제공 모듈.

inpath = "D:/Python/eclipse-workspace-Python/pythontest/excelfile"
outfile = "pandas_output6.xls"
# outfile = "pandas_output6.xlsx"
all_workbooks = glob.glob(os.path.join(inpath, "*.xls*"))  # 해당 폴더 아래의 xlsx, xls 모두 가능.
data_frames = []
for workbook in all_workbooks :
    all_workbooks = pd.read_excel(workbook, sheet_name=None, index_col=None)  # sheet 전체 읽어옴.
    for worksheet_name, data in all_workbooks.items() :
        data_frames.append(data)

# axis=0 : row 추가. 아래쪽으로 주르륵.
# axis=1 : column 추가. 옆쪽으로 주르륵.
all_data_concat = pd.concat(data_frames, axis=0, ignore_index=True)
writer = pd.ExcelWriter(outfile)
all_data_concat.to_excel(writer, sheet_name="all_data", index=False)
writer.save()