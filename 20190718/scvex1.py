'''
Created on 2019. 7. 18.

@author: gd_4

csvex1.py : csv 파일 예제.
'''
# import csv
import sys  # command에서 입력값 받기.
'''
    python csvex1.py in out -> 실행 명령문. python 실행파일명 입력파라미터 출력파라미터
    sys.argv[0] : csvex1.py -> 프로그램 이름. 고정되어 있음. 자바는 0부터 값을 입력 받음.
    sys.argv[1] : in
    sys.argv[2] : out
'''

# python csvex1.py jeju1.csv jeju1_bak.csv
input_file = sys.argv[1]  # jeju1.csv
output_file = sys.argv[2]  # jeju1_bak.csv

with open(input_file, "r", newline="") as filereader :  # "r" : 읽기 모드. t생략 되어져 있음. 파일 읽어서 filereader에 입력.
    with open(output_file, "w", newline="") as filewriter :  # filewriter에 쓰기.
        header = filereader.readline()  # 첫 번 째 줄 읽기.
        header = header.strip()  # 공백 제거. 자바의 trim() 메서드.
        header_list = header.split(",")  # , 를 기준으로 분리해서 list 로 저장. ["장소", "LON", "LAT"]
        filewriter.write(",".join(map(str, header_list)) + "\r\n")  # list의 각각의 요소를 문자열로 바꾸고 , 로 묶기. \r\n : 엔터(2byte)
        for row_list in filereader :  # 첫 번 째 줄(header)은 이미 읽었기 때문에 그 다음 줄부터 차례로 읽어옴. 한 번 읽으면 되돌아갈 수 없음.(stream)
            filewriter.write("".join(map(str, row_list)))  # header도 재조립할 필요 없이 이 방식으로 가능.
