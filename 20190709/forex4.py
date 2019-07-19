'''
Created on 2019. 7. 9.

@author: gd_4

forex4.py : *로 삼각형 출력하기.
*
**
***
****
*****

*****
****
***
**
*
'''
row = int(input("삼각형의 높이를 입력하세요."))
for i in range(1, row+1) :
    print("*"*i)
    
print()

for i in range(row, 0, -1) :
    print("*"*i)