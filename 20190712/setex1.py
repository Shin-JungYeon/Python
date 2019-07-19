'''
Created on 2019. 7. 12.

@author: gd_4

setex1.py : set 예제. 중복 불가. {}
'''
myset1 = {1, 2, 3, 4, 5}
myset2 = {4, 5, 6, 7}

numset1 = {1, 2, 3, 3, 4, 4, 5, 5, 6}
print(numset1)

# 집합 개념에 사용.
print("myset1 myset2 교집합 :", myset1 & myset2)  # 둘에게 모두 있는 값이면 출력.
print("myset1 myset2 교집합 :", myset1.intersection(myset2))

print("myset1 myset2 합집합 :", myset1 | myset2)  # 둘 중 하나에만 있는 값이어도 출력. 4, 5가 겹치는 값이지만 중복 불가이기때문에 한 번만 가져옴.
print("myset1 myset2 합집합 :", myset1.union(myset2))

print("myset1 myset2 차집합 :", myset1 - myset2)  # 앞에서 뒤를 뺀 나머지 값들 출력.
print("myset1 myset2 차집합 :", myset1.difference(myset2))

print("myset1 myset2 대칭차:", myset1 ^ myset2)  # 합집합 - 교집합
print("myset1 myset2 대칭차 :", myset1.symmetric_difference(myset2))
