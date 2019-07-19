'''
Created on 2019. 7. 9.

@author: gd_4

exam1.py : 문제
                        금액을 입력 받아 필요한 동전의 갯수를 출력하기.
                        단, 동전은 500, 100, 50, 10, 1 종류가 있다.
                        필요한 동전의 갯수는 최소로 한다.
'''
price = int(input("금액을 입력하세요."))
print("500원 갯수 :",price//500)
price = price % 500
print("100원 갯수 :",price//100)
price = price % 100
print("50원 갯수 :",price//50)
price = price % 50
print("10원 갯수 :",price//10)
price = price % 10
print("1원 갯수 :",price//1)