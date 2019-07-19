'''
Created on 2019. 7. 15.

@author: gd_4

varex1.py : 전역 변수 예제
'''
def func1() :
    global a  # a변수는 전역 변수의 a 변수를 사용함.
    a = 10  # 지역 변수로 선언 됨. 전역 변수보다 우선. 윗 줄에서 global 선언해주면 전역 변수를 가져와서 사용.
    print("func1() 변수 a : %d" % a)

def func2() :
    print("func2() 변수 a : %d" % a)
    
a = 20  # 전역 변수. 어디에서나 사용 가능한 변수.
func1()
func2()