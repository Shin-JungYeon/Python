'''
Created on 2019. 7. 30.

@author: gd_4

test6.py : 튜플을 생성하여 출력하기.
    ((1, 2, 3) (4, 5, 6) (7, 8, 9))
    
    1 2 3
    4 5 6
    7 8 9
    
    로 출력하기.
'''
tp = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for i in range(0, len(tp)) :
    for j in range(0, len(tp[i])) :
        print(tp[i][j], " ", end="")
    print()
