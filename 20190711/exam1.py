'''
Created on 2019. 7. 11.

@author: gd_4

exam1.py
    1. ss 문자 사이에 #문자를 넣어 출력하기.
    2. ss 문자를 거꾸로 출력하기.
'''
ss = "홍길동"
print("문제1. ss 문자 사이에 #문자를 넣어 출력하기.")
for i in range(0, len(ss)) :
    print(ss[i], end="#")

print()

print("문제2. ss 문자를 거꾸로 출력하기.")
print(ss[::-1])