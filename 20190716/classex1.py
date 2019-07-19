'''
Created on 2019. 7. 16.

@author: gd_4

classex1.py : 클래스 예제
    기본 생성자 제공 : __init__(self)
'''
class Car :
    color = ""
    speed = 0
    def __init__(self) :  # 기본 생성자의 형태.
        pass  # 함수는 있지만 내용이 없음을 의미.
        
    def upSpeed(self, value) :  # self = 자바의 this. 인스턴스 멤버.
        self.speed += value
    def downSpeed(self, value) :
        self.speed -= value
        
myCar1 = Car()  # 객체화. 기본 생성자 제공.
myCar1.color = "빨강"

myCar2 = Car()
myCar2.color="노랑"

myCar3 = Car()
myCar3.color="파랑"

myCar1.upSpeed(30)
print("자동차1 : 색상 = %s, 속도 = %d km/h" % (myCar1.color, myCar1.speed))
print("자동차2 : 색상 = %s, 속도 = %d km/h" % (myCar2.color, myCar2.speed))
print("자동차3 : 색상 = %s, 속도 = %d km/h" % (myCar3.color, myCar3.speed))