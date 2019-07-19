'''
Created on 2019. 7. 9.

@author: gd_4

forex2.py : 중첩반복문. 구구단 세로출력하기.
'''
i, j = 0, 0
for i in range(2, 10, 1) :
    for j in range(1, 10, 1) :
        print("%2d X %2d = %3d" % (i, j, (i*j)))  # 내부 for구문에 속한 내용.
    print()  # 외부 for구문에 속한 내용.