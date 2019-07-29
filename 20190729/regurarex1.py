'''
Created on 2019. 7. 29.

@author: gd_4

regurarex1.py : 정규식 예제
'''
import re  # 정규식 사용을 위한 모듈.
data = '''
    park 800905-1234567
    kim 700905-1234567
    choi 85010-a234567
'''
# 정규식을 사용하지 않은 경우.
result = []
for line in data.split("\n") :
    word_result = []
    for word in line.split(" ") :  # 이름과 주민 번호 구분.
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit() :
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 정규식을 사용한 경우.
print("정규식 사용하기.")
pat = re.compile("(\d{6})[-](\d{7})")  # \d{n} : 숫자 n자리로 이루어져 있는 부분. [-] : -이 문자임을 표시. pat : 정규식 객체.
print(pat.sub("\g<1>-*******", data))  # \g<1> : 첫번 째 그룹 값.

'''
    파이썬의 기본 정규식 표현. 문서 표현 방식.
    () : 그룹 지정.
    [] : 문자 의미.
    {n} : n개.
    \d : 숫자.
        => (\d{6})[-](\d{7}) : 첫 번 째 그룹 : 숫자 6자리, 다음은 - 문자, 두 번 째 그룹 : 숫자 7자리.
    
    \g<n> : n번 째 그룹.
    ? : 0 또는 1개.
        => ca?t : a문자가 없거나 1개인 경우.
                  "ct" : true
                  "cat" : true
                  "caaaaat" : false
    * : 0개 이상.
        => ca*t : a문자가 없거나 여러 개인 경우.
                  "ct" : true
                  "cat" : true
                  "caaaaat" : true
    + : 1개 이상.
        => ca+t : a문자가 1개 이상인 경우. 없으면 안됨.
                  "ct" : false
                  "cat" : true
                  "caaaaat" : true
    {n} : n개 반복.
        => ca{2}t : a문자가 2개인 경우.
                  "ct" : false
                  "cat" : false
                  "caat" : true
                  "caaaaat" : false
    {n, m} : n개 ~ m개 반복.
        => ca{2, 5}t : a문자가 2개인 경우.
                  "ct" : false
                  "cat" : false
                  "caat" : true
                  "caaat" : true
                  "caaaaat" : true
                  "caaaaaaaaat" : false
'''