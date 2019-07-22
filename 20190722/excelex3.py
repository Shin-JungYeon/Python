'''
Created on 2019. 7. 22.

@author: gd_4

excelex3.py : excel 파일을 읽어서 excel 파일로 생성하기.
'''
from xlrd import open_workbook
from xlwt import Workbook  # pip3 install xlwt

infile = "ssec1804.xls"  # 원본 excel 파일의 이름.
outfile = "ssec1804out.xls"  # 새로 저장될 excel 파일의 이름.

out_workbook = Workbook()  # excel 파일 전체에 해당하는 객체. 현재는 빈 객체.
out_sheet = out_workbook.add_sheet("전체증감")  # sheet 한 개 추가.

with open_workbook(infile) as workbook :  # 원본 excel 파일 전체.
    worksheet = workbook.sheet_by_name("1.전체증감")  # sheet_by_name() : sheet 이름으로 가져옴.
    for row_index in range(worksheet.nrows) :
        for col_index in range(worksheet.ncols) :
            out_sheet.write(row_index, col_index, worksheet.cell_value(row_index, col_index))  # 각 셀들을 저장.
        print(worksheet.cell_value(row_index, col_index))

# out_workbook 에는 "ssec1804.xls" 엑셀 파일의 1.전체증감 이름의 sheet의 내용을 저장하고 있는 데이터 객체.
out_workbook.save(outfile)  # 데이터를 outfile 파일로 저장.