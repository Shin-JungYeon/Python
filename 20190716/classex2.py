'''
Created on 2019. 7. 16.

@author: gd_4

classex2.py : 생성자를 이용한 객체 생성.
'''
class Car :
    color = ""  # 인스턴스 변수. self로 접근 가능.
    speed = 0  # 인스턴스 변수.
    
    def __init__(self, v1, v2) :  # 생성자
        self.color = v1
        self.speed = v2
        
    def upSpeed(self, value) :  # self = 자바의 this. 인스턴스 멤버.
        self.speed += value
    def downSpeed(self, value) :
        self.speed -= value

myCar1 = Car("빨강", 30)  # ("빨강", 30) -> (v1, v2)
myCar2 = Car("노랑", 20)

print("자동차1 : 색상 = %s, 속도 = %d km/h" % (myCar1.color, myCar1.speed))
print("자동차2 : 색상 = %s, 속도 = %d km/h" % (myCar2.color, myCar2.speed))