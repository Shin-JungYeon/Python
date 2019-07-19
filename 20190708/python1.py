'''
Created on 2019. 7. 8.

@author: gd_4

python1.py
파이썬에서의 여러 줄 주석 부분.

변수 선언 부분이 없음.
처음 값이 들어갈 때 자료형 결정.
입력값에 맞게 자동 변경됨.

if 사용할 때 자바는 {}가 있지만 파이썬에서는 공백으로 구분. 사용시 주의해야 함.

1. 변수 선언 필요 없음.
2. 조건문, 반복문의 내부 구문은 공백으로 구분함. 강제로 줄맞춤 필요.
3. ''' ''' : 여러줄 주석.
4. # : 한줄 주석.
'''
sel = int(input('입력 진수 결정(16/10/8/2) : '))
num = input("값 입력 : ")
if sel == 16 :
    num10 = int(num, 16)  # num을 16진수로 인식한 정수 저장.
    print("hello world")  # sel 값이 16일 때만 실행.
print("hello world")  # sel 값과 상관없이 무조건 실행.
if sel == 10 :
    num10 = int(num, 10)
if sel == 8 :
    num10 = int(num, 8)
if sel == 2 :
    num10 = int(num, 2)
print("16진수 -->", hex(num10))
print("10진수 -->", num10)
print("8진수 -->", oct(num10))
print("8진수 -->", bin(num10))