'''
Created on 2019. 7. 10.

@author: gd_4

listex1.py : list 예제

collection
    1. list
    2. dictionary : (Map) key와 value의 쌍.
    3. tuple : 변경 불가 list.
'''
a = [0, 0, 0, 0]
hap = 0
for i in range(0, 4) :
    a[i] = int(input(str(i+1) + "번 째 값 : "))
    hap += a[i]
print("합계 :", hap)
