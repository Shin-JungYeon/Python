'''
Created on 2019. 7. 9.

@author: gd_4

forex3.py : 중첩반복문. 구구단 가로출력하기.
'''
i, j = 0, 0
for i in range(0, 10, 1) :
    for j in range(2, 10) :  # range에서 증감값이 1이면 생략 가능.
        if i == 0 :
            print("%3d단" % j, end="     ")
        else :
            print("%2d X %d = %2d" % (j, i, (i*j)), end="   ")  # 내부 for구문에 속한 내용.
    print()