'''
Created on 2019. 7. 16.

@author: gd_4

classex5.py
'''
class Line :
    length = 0
    
    def __init__(self, length) :  # 1. 생성자. 객체 생성.
        self.length = length
        print("선 길이 :", self.length, "Line 객체 생성.")
    def __del__(self) :  # 5. 프로그램 종료 후 실행. 소멸자. 개체 소멸 직전에 호출. 메모리 클리어. 자바에서는 가비지 콜렉터에서 자동으로 정리.
        print("선 길이 :", self.length, "Line 객체 제거.")
    def __repr__(self) :  # 2. 객체를 문자열화. 자바의 toString() 메서드와 같은 역할.
        return "선 길이 : " + str(self.length)
    # 연산자 오버로딩.
    def __add__(self, other) :  # 3. 객체끼리 + 연산을 했을 경우 호출 됨. other에 Line 객체 들어옴.
        print("더하기 연산 호출.")
        return self.length + other.length
    def __lt__(self, other) :  # 4-1.
        print("< 연산 호출.")
        return self.length < other.length
    def __gt__(self, other) :  # 4-3.
        print("> 연산 호출.")
        return self.length > other.length
    def __eq__(self, other) :  # 4-2.
        print("== 연산 호출.")
        return self.length == other.length
    
    
myLine1 = Line(200)  # 객체 생성. -> 생성자 호출.
myLine2 = Line(100)  # 객체 생성. -> 생성자 호출.
print()
print(myLine1)  # myLine1은 객체. 
print(myLine2)
print()

print("두 선의 합 :", myLine1 + myLine2)  # 원래는 더하기 연산이 불가능. 객체 간의 더하기 연산을 할 경우 __add__ 메서드 호줄.
print()

if myLine1 < myLine2 :  # __lt__ 메서드 호출.
    print("myLine1의 길이가 짧다.")
elif myLine1 == myLine2 :  # __eq__ 메서드 호출.
    print("두 선의 길이가 같다.")
if myLine1 > myLine2 :  # __gt__ 메서드 호출.
    print("myLine1의 길이가 길다.")

print()
print("프로그램 종료.")
print()