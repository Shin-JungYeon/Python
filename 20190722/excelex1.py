'''
Created on 2019. 7. 22.

@author: gd_4

excelex1.py : excel(.xlsx) 파일 읽기.
    두 확장자의 접근 방식이 다름. 엑셀 파일의 구조가 다르기 때문.
    xlsx : pip3 install openpyxl
    xls  : pip3 install xlrd
'''
import openpyxl

book = openpyxl.load_workbook("sales_2015.xlsx")  # 엑셀 파일 읽어서 book 에 저장.
sheet = book.worksheets[0]  # 엑셀 파일은 csv파일과 다르게 sheet를 연결 시킬 수 있음.
data = []
for row in sheet.rows :
    line = []
    # l : 컬럼 순서.
    # d : 데이터 객체.
    for l, d in enumerate(row) :  # enumerate : 열거형. 셀 별로 나열.
        line.append(d.value)  # list 형태.
    print(line)
    data.append(line)
# print(data)