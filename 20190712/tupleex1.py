'''
Created on 2019. 7. 12.

@author: gd_4

tupleex1.py
    list       : 가변 배열. []
    dictionary : Map. {key:value}
    tuple      : 변경 불가 list. ()
'''
mytuple = (10, 20, 30)
# mytuple.append(40)  # 오류 발생. 튜플은 변경 불가.
print(type(mytuple))
print(mytuple)

mylist = list(mytuple)
mylist.append(40)
print(type(mylist))
print(mylist)

# list를 거쳐서 변경해야 함.

mytuple = tuple(mylist)
print(type(mytuple))
print(mytuple)
print()

print(mytuple[0], mytuple[1], mytuple[2], mytuple[3])  # list처럼 사용 가능.
print(mytuple[1:3])
print(mytuple[:3])
print(mytuple[2:])
print(mytuple[::2])