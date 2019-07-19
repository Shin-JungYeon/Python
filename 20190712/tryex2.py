'''
Created on 2019. 7. 12.

@author: gd_4

tryex1.py : 다중 예외 처리.
'''
num1 = input("문자 1 입력 : ")
num2 = input("문자 2 입력 : ")

try :
    num1 = int(num1)
    num2 = int(num2)
    res = num1/num2
    print("결과 :", res)
except ValueError :
    print("숫자만 입력이 가능합니다.")
except ZeroDivisionError :
    print("num2에 0이 입력되었습니다. 0으로는 나눌 수 없습니다.")
except KeyboardInterrupt :
    print("입력란에 Ctrl+c 키가 눌렸습니다.")
finally :
    print("finally 구문 실행")
print("프로그램 종료")