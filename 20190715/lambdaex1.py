'''
Created on 2019. 7. 15.

@author: gd_4

lambdaex1.py : 람다식으로 함수 구현하기.
'''
def hap(num1, num2) :
    res = num1 + num2
    return res

print(hap(10, 20))

hap2 = lambda num1, num2 : num1 + num2  # 람다 함수 선언.
print(hap2(10, 20))

hap2 = lambda num1, num2 : num1 * num2
print(hap2(10, 20))

hap3 = lambda num1=10, num2=20 : num1 + num2  # num1=10, num2=20 : default 매개 변수. 매개 변수의 기본값 설정.
print(hap3())
print(hap3(100))  # 매개 변수의 앞순서 부터 입력 됨.
print(hap3(100, 200))
# print(hap3(100, 200, 300))  # 오류. hap3()는 매개 변수 2개밖에 못 받음.