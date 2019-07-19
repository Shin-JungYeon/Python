'''
Created on 2019. 7. 15.

@author: gd_4

strex1.py
'''
instr = input("문자를 입력하세요. ")
if instr.isdigit() :  # 문자열이 숫자인 경우.
    print("숫자입니다.")
elif instr.isalpha() :  # 문자인 경우. 한글, 영어 모두 가능.(대소문자 구분 불가.)
    print("문자입니다.")
elif instr.isalnum() :  # 숫자와 문자가 모두 있을 경우.
    print("숫자 또는 문자입니다.")
else :
    print("모르겠습니다.")
    
if instr.islower() :
    print("소문자입니다.")
elif instr.isupper() :
    print("대문자입니다.")
elif instr.isspace() :
    print("공백입니다.")
else :
    print("구분 못합니다.")