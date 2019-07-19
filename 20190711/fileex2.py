'''
Created on 2019. 7. 11.

@author: gd_4

fileex2.py : utf8 파일 읽기 예제
'''
infp = None
inStr = ""
# infp = open("c:/temp1/data1utf8.txt")  # 인코딩 방식이 기본 설정된 방식이 아니면 읽어올 수 없음.
infp = open("c:/temp1/data1utf8.txt", "r", encoding="utf-8")  # 인코딩 방식 설정 필요.
while True :
    inStr = infp.readline()
    if not inStr :
        break
    print(inStr, end="")
infp.close()