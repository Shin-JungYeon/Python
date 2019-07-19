'''
Created on 2019. 7. 10.

@author: gd_4

whileex1.py : while 구문 예제
'''
i, hap = 0, 0
while i<11 :
    hap = hap + i
    i = i + 1
print("1부터 10까지의 합 :", hap)

while True :
    a = int(input("첫번째 숫자를 입력하세요. (종료 : 0) : "))
    if a == 0 :
        break
    b = int(input("두번째 숫자를 입력하세요. : "))
    hap = a + b
    print("%d + %d = %d" % (a, b, hap))
print("프로그램 종료")