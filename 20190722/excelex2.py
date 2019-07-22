'''
Created on 2019. 7. 22.

@author: gd_4

excelex2.py : excel(.xls) 파일 읽기. 
'''
from xlrd import open_workbook

workbook = open_workbook("ssec1804.xls")
print("worksheets의 갯수 :", workbook.nsheets)
for worksheet in workbook.sheets() :
    print("worksheet 이름 :", worksheet.name, "\n행 수 :", worksheet.nrows,
          "\n컬럼 수 :", worksheet.ncols)