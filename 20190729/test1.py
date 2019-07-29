'''
Created on 2019. 7. 29.

@author: gd_4

test1.py
    16진수 한 문자를 입력받아서 10진수로 출력하기.
    16진수 문자가 아닌 경우 16진수 아님 출력하기.
'''
num16 = input("16진수 한 문자를 입력하세요.")
if (num16 >= "0" and num16 <= "9") or (num16 >= "a" and num16 <= "f") or (num16 >= "A" and num16 <= "F") :    
    print("16진수", num16, "=", int(num16, 16))
else :
    print("16진수가 아닙니다.")