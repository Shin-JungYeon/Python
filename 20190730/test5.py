'''
Created on 2019. 7. 30.

@author: gd_4

test5.py
    aa 리스트에 3의 배수 200개 저장.
    aa 리스트의 역순인 bb 리스트 구하기.
    bb[0]과  bb[199]를 출력하기.
'''
aa = []
bb = []

num, cnt = 1, 0
while True :
    num += 1
    if num%3 == 0 :
        aa.append(num)
        cnt += 1
    if cnt == 200 :
        break
print(aa)
print(len(aa))

bb = aa[::-1]
print(bb[0], bb[199])