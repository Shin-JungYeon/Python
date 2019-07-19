'''
Created on 2019. 7. 9.

@author: gd_4

opex1.py : 연산자 연습
두 개의 정수를 입력받아서 +,-,*,/,% 연산 후의 결과를 출력하기.
        // : 나눗셈 후 소숫점 이하는 버리고 몫을 가져옴.
        ** : 제곱.
문자열 연결 : + 연산 사용.
         * 연산 사용.
'''
num1 = int(input("첫번째 정수를 입력하세요."))
num2 = int(input("두번째 정수를 입력하세요."))
print(num1, "+", num2, "=", (num1+num2))
print(num1, "-", num2, "=", (num1-num2))
print(num1, "*", num2, "=", (num1*num2))
print(num1, "^", num2, "=", (num1**num2))
print(num1, "/", num2, "=", (num1/num2))  # 정수끼리 계산한 결과가 정수가 아님.
print(num1, "/", num2, "=", (num1//num2))  # 소숫점 이하는 버리고 몫만 보여주는 연산자.
print(num1, "%", num2, "=", (num1%num2))

print("a"+"b"+"c")
print("abc"*3)  # abc 라는 문자열을 3번 연속 출력.