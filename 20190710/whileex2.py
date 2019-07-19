'''
Created on 2019. 7. 10.

@author: gd_4

whileex1.py : 랜덤 함수를 사용하여 숫자 맞추기.
    컴퓨터가 1부터 100까지 임의의 수를 저장하고,
    화면에 숫자를 입력받아 컴퓨터가 저장한 수 맞추기.
    입력된 수가 저장된 수보다 크면 '작은 수를 입력하세요.' 메세지 출력.
    입력된 수가 저장된 수보다 작으면 '큰 수를 입력하세요.' 메세지 출력.
    저장된 수와 입력된 수가 같은 경우 프로그램 종료.
    입력 건수를 화면에 출력하기.
'''
import random
rnum = random.randrange(0, 100)
print("저장된 수 : %d" % rnum)
cnt = 0
inputnum = int(input("1부터 100까지의 수 중 하나를 입력하세요. : "))
while True :
    cnt = cnt + 1
    if inputnum > rnum :
        inputnum = int(input("작은 수를 입력하세요. : "))
    elif inputnum < rnum :
        inputnum = int(input("큰 수를 입력하세요. : "))
    else :
        print("정답입니다.")
        break
print("%d번 만에 맞췄습니다." % cnt)