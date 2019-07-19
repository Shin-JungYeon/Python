'''
Created on 2019. 7. 16.

@author: gd_4

classex4.py : 파이썬에서의 상속 구현.
'''
class Car :
    speed = 0
    def upSpeed(self, v) :
        self.speed += v
        print("현재 속도 :", self.speed)
        
class Sedan(Car) :
    def upSpeed(self, v) :  # 오버라이딩.
        self.speed += v
        if self.speed > 150 :
            self.speed = 150
        print("현재 속도(Sedan) :", self.speed)
        
class Truck(Car) :
    pass  # Car랑 똑같음. 단순 상속.


c1 = Car()
s1 = Sedan()
t1 = Truck()

print("트럭 : ", end="")
t1.upSpeed(200)

print("승용차 : ", end="")
s1.upSpeed(200)

print("자동차 : ", end="")
c1.upSpeed(200)