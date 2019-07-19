'''
Created on 2019. 7. 11.

@author: gd_4

fileex4.py : 파일 복사하기. fileex1.py 파일을 읽어서 fileex1.bak 파일로 저장하기.
'''
infp = None
outfp = None
inStr = ""

# infp = open("D:/Python/eclipse-workspace-Python/pythontest/20190711/fileex1.py", "r", encoding="utf-8")  # python은 반드시 utf-8로 저장.
infp = open("fileex1.py", "r", encoding="utf-8")  # 현재 작업 폴더에 있는 파일은 경로 안써줘도 됨.
outfp = open("fileex1.bak", "w")

while True :
    inStr = infp.readline()
    if not inStr :
        break
    print(inStr, end="")
    outfp.writelines(inStr)
infp.close()