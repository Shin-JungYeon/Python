'''
Created on 2019. 7. 15.

@author: gd_4

mapex2.py : 람다식을 이용한 map
'''
def hap(n1, n2) :
    result = n1 + n2
    return result

myList = [1, 2, 3, 4, 5]
add10 = lambda num : num + 10
myList = list(map(add10, myList))  # 각각의 요소에 add10함수 적용.
print(myList)

myList = list(map(lambda num : num + 10, myList))
print(myList)

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
haplist = list(map(lambda n1, n2 : n1 + n2, list1, list2))
print(haplist)

# 람다식을 함수형태로 구현.
haplist2 = []
for i in range(len(list1)) :
    haplist2.append(hap(list1[i], list2[i]))
print(haplist2)