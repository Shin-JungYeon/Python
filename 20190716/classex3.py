'''
Created on 2019. 7. 16.

@author: gd_4

classex3.py : 클래스 변수. 파이썬에서는 static이라는 예약어 없음.
'''
class Car :
    color = ""  # 인스턴스 변수. self로 접근 가능.
    speed = 0  # 인스턴스 변수.
    count = 0  # 클래스 변수.
    
    def __init__(self) :  # 생성자
        self.speed = 0
        Car.count += 1  # self.count로 하면 인스턴스 변수로 사용됨.

myCar1, myCar2 = None, None

myCar1 = Car()
myCar1.speed = 30
# print("자동차1 : 속도 = %d km/h, 생산번호 = %d" % (myCar1.speed, myCar1.count))
print("자동차1 : 속도 = %d km/h, 생산번호 = %d" % (myCar1.speed, Car.count))  # 클래스 변수의 사용. speed도 Car.speed로 사용해도 오류가 발생하지 않음.

myCar2 = Car()
myCar2.speed = 20
# print("자동차2 : 속도 = %d km/h, 생산번호 = %d" % (myCar2.speed, myCar2.count))
print("자동차2 : 속도 = %d km/h, 생산번호 = %d" % (myCar2.speed, Car.count))