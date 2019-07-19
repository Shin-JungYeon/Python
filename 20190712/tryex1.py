'''
Created on 2019. 7. 12.

@author: gd_4

tryex1.py : 예외 처리 예제. 예외가 발생하면 내가 처리.
'''
mystr = "파이썬을 공부 중입니다. 파이썬은 재미있습니다."
strPosList = []  # list
index = 0
while True :
    try :
        index = mystr.index("파이썬", index)  # index("파이썬", index) : "파이썬"을 index 이후부터 찾기. 파이썬 문자열의 시작 위치 index 값 리턴.
        strPosList.append(index)  # 위치 인덱스 값을 list에 추가.
        index += 1
    except :  # 찾는 문자가 없으면 예외 발생.
        break
print("파이썬 문자 위치 :", strPosList)
