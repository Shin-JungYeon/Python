'''
Created on 2019. 7. 29.

@author: gd_4

regurarex2.py
'''
import re
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()  # 문자열을 공백으로 구분해서 list 객체로 저장.

pattern = re.compile(r"The", re.I)  # r"The" : row 문자열. re.I : 대소문자 구별하지 않음.
count = 0
for word in string_list :
    if pattern.search(word) :  # pattern과의 일치여부 확인.
        count += 1
print("output #1 : {0:d} ".format(count))
print()

# match_word : The 문자를 대소문자 구분 없이 match_word 라는 그룹으로 생성.
pattern = re.compile(r"(?P<match_word>The)", re.I)
print("output #2 :")
for word in string_list :
    if pattern.search(word) :
        print("{0}".format(pattern.search(word).group("match_word")))
string_to_find = r"The"
print()

pattern = re.compile(string_to_find, re.I)
print("output #3 : {0}".format(pattern.sub("a", string)))  # 패턴에 맞는 문자를 전부 a로 바꿔줌.