'''
Created on 2019. 7. 8.

@author: gd_4

ifex1.py : if, else 예제
'''
score = int(input("점수를 입력하세요. (0 ~ 100) : "))

print("if else")
if score >= 90 :
    print("A학점")
else :
    if score >= 80 :
        print("B학점")
    else :
        if score >= 70 :
            print("C학점")
        else :
            if score >= 60 :
                print("D학점")
            else :
                print("F학점")

print("if elif")
if score >= 90 :
    print("A학점")
elif score > 80 :
    print("B학점")
elif score > 70 :
    print("C학점")
elif score > 60 :
    print("D학점")
else : 
    print("F학점")