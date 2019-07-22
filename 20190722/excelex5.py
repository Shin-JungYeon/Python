'''
Created on 2019. 7. 22.

@author: gd_4

excelex5.py : excelex4.py 를 함수형태로 바꾸기.
'''
from xlrd import open_workbook
from xlwt import Workbook  # pip3 install xlwt

def makesheet(out_sheet) :
    for row_index in range(worksheet.nrows) :
        for col_index in range(worksheet.ncols) :
            out_sheet.write(row_index, col_index, worksheet.cell_value(row_index, col_index))

infile = "ssec1804.xls"  # 원본 excel 파일의 이름.
outfile = "ssec1804mf2.xls"  # 새로 저장될 excel 파일의 이름.

out_workbook = Workbook()  # excel 파일 전체에 해당하는 객체. 현재는 빈 객체.
out_sheet_m = out_workbook.add_sheet("남자")  # sheet 한 개 추가.
out_sheet_f = out_workbook.add_sheet("여자")  # sheet 한 개 추가.

with open_workbook(infile) as workbook :
    # worksheet : 전역변수.
    worksheet = workbook.sheet_by_name("1.남자")
    makesheet(out_sheet_m)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(out_sheet_f)
    
out_workbook.save(outfile)