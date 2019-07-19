'''
Created on 2019. 7. 15.

@author: gd_4

fiboex1.py : 피보나치 수열 구하기.
    피보나치 수열 : 0, 1, 1(0+1), 2(1+1), 3(1+2), 5(2+3), 8(3+5), 13, 21, ...
        입력값 : 5 -> 0, 1, 1, 2, 3
        입력값 : 10 -> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
'''
def fibo(n) :
    global num1, num2, num3
#     global fibolist  # 명확하게 하기 위해서는 global 로 선언해주는 것이 좋음. 안해줘도 알아서 가져옴.
    fibolist.append(num1)  # global 해주지 않으면 전역변수여도 함수 내에서는 그대로 사용하지 못함. ???
    fibolist.append(num2)
    fibolist.append(num3)
    for i in range(3, n) :
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        fibolist.append(num3)

fibolist = []
num1 = 0
num2 = 1
num3 = 1

num = int(input("피보나치 수열을 구할 갯수를 입력하세요. (단 3 이상의 값으로 입력.) : "))
print("f(", num, ") = ", end="")
fibo(num)
print(fibolist)