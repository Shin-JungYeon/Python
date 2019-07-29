'''
Created on 2019. 7. 29.

@author: gd_4

comprehensionex1.py : 컴프리헨션 예제
    컴프리헨션 : 함수로 리스트를 작성하는 기능.
'''
mylist = []
for i in range(1, 6) :
    mylist.append(i)
print(mylist)

# 컴프리헨션으로 리스트 표현하기.
mylist = [num for num in range(1, 6)]
print(mylist)
print([num for num in range(1, 6)])
print([num*2 for num in range(1, 6)])
print()

# 1부터 10까지의 숫자 중 짝수로 이루어진 리스트 생성.
even_list = []
for n in range(1, 11) :
    if n % 2 == 0 :
        even_list.append(n)
print(even_list)

print("컴프리헨션 방식으로 코딩하기.")
print([num for num in range(1, 11) if num%2==0])
print([num for num in range(2, 11, 2)])  # 2 부터 10 까지 2씩 증가.
print()

print("1부터 100까지의 숫자 중 3의 배수로 이루어진 리스트 생성하기.")
print([num for num in range(1, 100) if num%7==0])
print()

foods = ["쌈밥", "치킨", "피자"]
sides = ["사과", "콜라", "커피"]
print([(x, y) for x in foods for y in sides])  # 두 개의 리스트 join. 중첩 반복문처럼 실행.
print()

print("1부터 100까지의 숫자 중 2의 배수이면서 3의 배수인 리스트 생성하기.")
print([num for num in range(1, 100) if num%2==0 if num%3 == 0])  # if 조건문도 중첩 가능.