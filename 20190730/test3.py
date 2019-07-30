'''
Created on 2019. 7. 30.

@author: gd_4

test3.py : 삼각형 그리기.

    삼각형의 종류와 높이를 입력받아 다음 삼각형 그리기.
    종류 1 : 직각 삼각형        종류 2 : 역 직각 삼각형        종류 3 : 이등변 삼각형
    *                *****
    **               ****
    ***              ***
    ****             **
    *****            *
'''
kind = int(input("삼각형의 종류를 입력하세요.(1, 2, 3)"))
row = int(input("삼각형의 높이를 입력하세요."))

if kind == 1 :
    for i in range(1, row+1) :
        print("*" * i)  # i번 출력.

elif kind == 2 :
    for i in range(row, 0, -1) :
        print("*" * i)

elif kind == 3 :
    for i in range(1, row+1) :
        num = row - i
        sp = " " * num
        star = "*" * ((i*2)-1)
        print(sp + star)
else :
    print("삼각형의 종류를 잘못 입력하였습니다.")