'''
Created on 2019. 7. 12.

@author: gd_4

functionex1.py
'''
def myFunc() :  # 함수 정의. 실행이 아님.
    print("myFunc() 함수 호출.")  # 5.

def main() :  # 함수 정의. 실행이 아님.
    print("main() 함수에서 myFunc() 함수 호출.")  # 3.
    myFunc()  # 4. myFunc() 함수 호출.
    print("전역 변수 gvar 값 :", gvar)  # 6.
    
gvar = 100  # 전역 변수. 클래스, 함수에 상관없이 사용 가능.

if __name__ == '__main__' :  # 1. 프로그램이 시작을 할 때 시작 부분 설정. 자바의 main
#     gvar = 200  # 모든 함수에서 값이 200으로 변경.
    main()  # 2. main() 함수 호출.