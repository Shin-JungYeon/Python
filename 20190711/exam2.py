'''
Created on 2019. 7. 11.

@author: gd_4

exam2.py : 문자열 '(문자)' 로 입력 받기. ()가 없는 경우 ()를 추가하기.
    startswith, endswith 메서드 이용하기.
'''
# str = input("문자를 입력하세요 : ")
# if str.startswith('(') & str.endswith(')') :
#     print(str)
# elif str.startswith('(') & (not str.endswith(')')) :
#     print(str,")")
# elif (not str.startswith('(')) & str.endswith(')') :
#     print(str,")")
# else :
#     print("(",str,")")

ss = input("문자를 입력하세요 : ")
print("출력 문자열 : ", end="")
result = ""
if not ss.startswith("(") :
    result += "("
result += ss
if not ss.endswith(")") :
    result += ")"
print(result)
