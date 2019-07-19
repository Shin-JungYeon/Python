'''
Created on 2019. 7. 11.

@author: gd_4

fileex3.py : 콘솔에서 입력 받은 내용 파일에 쓰기.
'''
outfp = None
outfp = open("c:/temp1/data2.txt", "w")  # 파일 읽기, 쓰기 모두 open 사용.
while True :
    outStr = input("내용 입력.")
    if outStr != "" :
        outfp.writelines(outStr + "\n")
    else :
        break
outfp.close()
print("프로그램 종료.")
