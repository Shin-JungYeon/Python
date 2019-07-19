'''
Created on 2019. 7. 17.

@author: gd_4

threadex1.py : 스레드 구현하기.
'''
import threading  # 모듈
import time

class RacingCar :
    carName = ""
    
    def __init__(self, name) :
        self.carName = name
    def runCar(self) :
        for _ in range(1, 3) :  # _ 라는 이름을 가진 변수. 이름으로 아무것도 안쓰겠다는 의미. 그냥 단순히 1부터 3까지 3번 반복.
            carStr = self.carName + " 달립니다.\n"
            print(carStr, end="")
            time.sleep(0.1)  # 0.1초 대기.
            
car1 = RacingCar("자동차1")
car2 = RacingCar("자동차2")
car3 = RacingCar("자동차3")

th1 = threading.Thread(target=car1.runCar)  # 스레드 객체 생성. target : 스레드의 대상.
th2 = threading.Thread(target=car2.runCar)
th3 = threading.Thread(target=car3.runCar)

th1.start()  # 스레드 환경으로 시작.
th2.start()
th3.start()
th1.join()  # 스레드가 종료할 때까지 메인은 대기. -> 프로그램 종료. 가장 마지막에 출력.
th2.join()
th3.join()

print("프로그램 종료.")