'''
Created on 2019. 7. 12.

@author: gd_4

exam1.py
'''
# 1. 주민번호의 생년월일과 이후 부분을 출력하기.
jumin = "940401-2134567"
birth = jumin[:6]
after = jumin[7:]
gender = jumin[7]
print("생년월일 :", birth)
print("생년월일 이후 :", after)
print("성별코드 :", gender)
print()

# 2. list1 의 내용을 [7, 5, 3, 1]로 출력하기.
list1 = [1, 3, 5, 7]
print(list1[::-1])
print()

# 3. list2 를 list is short 문자열로 출력하기.
list2 = ["life", "is", "short"]
print(" ".join(list2))  # 해당 문자열과 각 요소를 합쳐서 출력.
print()

# 4. dic1 에서 F를 제거하고 값을 출력하기. F를 제외한 다른 내용만 출력하기.
dic1 = {"A":90, "B":80, "C":70, "D":60, "F":50}
print("제거된 F의 값 :", dic1.pop("F"))
print("F 제거된 이후의 값들 :", dic1)
print()

# 5. list3 의 요소들의 중복을 제거하기.
list3 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
listToSet = set(list3)  # set으로 바꾸면 자동으로 중복이 제거됨.
list3 = list(listToSet)
print(list3)

