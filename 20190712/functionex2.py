'''
Created on 2019. 7. 12.

@author: gd_4

functionex2.py
'''
def getMeen(numlist) :  # 매개변수, 리턴값 자료형 없어도 됨. \ : 다음 줄도 함수의 내용임. 원래는 한 줄로 작성.
    return sum(numlist) / len(numlist) \
        if len(numlist) > 0 \
        else float("NaN")  # if문의 순서가 뒤에 있음. 조건에 따라 리턴타입이 달라짐. -> 파이썬이니까 가능.

mylist = [2, 2, 2, 4, 4, 6, 6, 8, 8]
print("mylist의 평균 : {!s}".format(getMeen(mylist)))

emptylist = []
print("emptylist의 평균 : {!s}".format(getMeen(emptylist)))

mytuple = ("x","y","z")
one, two, three = mytuple  # 순서대로 값 들어감.
print("tuple : {0}, {1}, {2}".format(one, two, three))

mytuple = (10, 20, 30, 40)
print("mytuple 평균 : {!s}".format(getMeen(mytuple)))