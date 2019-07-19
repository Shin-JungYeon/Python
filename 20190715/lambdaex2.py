'''
Created on 2019. 7. 15.

@author: gd_4

lambdaex2.py : 람다식을 이용한 리스트 처리
'''
myList = [1, 2, 3, 4, 5]

def add10(num) :
    return num + 10

for i in range(len(myList)) :
    myList[i] = add10(myList[i])
    
print(myList)

# add20 : add10 함수를 람다형태로 구현.
add20 = lambda num : num + 10
for i in range(len(myList)) :
    myList[i] = add20(myList[i])

print(myList)