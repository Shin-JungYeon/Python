'''
Created on 2019. 7. 11.

@author: gd_4

fileex1.py : 파일 읽기 예제
    open(파일 이름, 파일 모드)
    - 파일모드 
        "r" : 읽기 모드. 기본값.
        "w" : 쓰기 모드. 존재하지 않는 파일은 생성해줌.
        "r+" : 읽기/쓰기 겸용.
        "a" : append 모드. 쓰기 모드. 내용을 추가함. 존재하지 않는 파일은 생성해줌.
        "t" : text 모드로 읽고 쓰기. 문자열형 파일. 기본값.
        "b" : binary 모드로 읽고 쓰기. 바이트형 파일.
'''
infp = None
inStr = ""
infp = open("c:/temp1/data1.txt", "rt")  # "rt" 모드가 기본값이므로 생략 가능.
# inStr = infp.readline()  # enter값까지 읽어옴.
# print(inStr, end="")
# inStr = infp.readline()
# print(inStr, end="")
# inStr = infp.readline()
# print(inStr, end="")

# 파일 내용 전부 읽기 : readlines()
# inStr = infp.readlines()  # list. 한 번 읽어오면 사용 불가.
# print(inStr)
# for s in inStr :
#     print(s, end="")
# infp.close()  # 사용 후 꼭 닫아주기.

# 반복문을 이용하여 한 줄 씩 읽기 : readline() 사용.
while True :
    inStr = infp.readline()
    if not inStr :
        break
    print(inStr, end="")
infp.close()