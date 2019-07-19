'''
Created on 2019. 7. 9.

@author: gd_4
\
forex1.py : for 반복문 예제
'''
i, hap = 0, 0  # 변수 여러개 초기화 한 번에 가능.
n1, n2, n3 = 0, 0, 0
n1 = int(input("시작 숫자 입력 : "))
n2 = int(input("종료 숫자 입력 : "))
n3 = int(input("증감 숫자 입력 : "))

for i in range(n1, n2+1, n3) :  # for(int i=n1; i<n2+1; n3) {...}
    hap = hap + i

print("%d부터 %d까지 %d 증감한 값의 합 : %d" % (n1, n2, n3, hap))