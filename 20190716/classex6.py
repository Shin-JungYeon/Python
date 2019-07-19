'''
Created on 2019. 7. 16.

@author: gd_4

classex6.py : 추상 메서드 예제  : 구현부가 없음. 하위 클래스에서 반드시 오버라이딩이 필요함. 
'''
class SuperC :
    # 추상 메서드로 구현됨. 하위 클래스에서 반드시 오버라이딩이 필요함.
    def method(self) :
        raise NotImplementedError
    def method2(self) :
        print("SuperC의 method() 호출. 부모클래스의 메서드.")

class SubC1(SuperC) :
#     def method(self) :
#         print("SubC1의 method() 호출. 오버라이딩 됨.")
    def method2(self) :
        print("SubC1의 method2() 호출. 오버라이딩 됨.")

class SubC2(SuperC) :
#     def method(self) :
#         print("SubC2의 method() 호출. 오버라이딩 됨.")
    def method2(self) :
        print("SubC2의 method2() 호출. 오버라이딩 됨.")


sub1 = SubC1()
sub2 = SubC2()
# sub1.method()
# sub2.method()
sub1.method2()
sub2.method2()