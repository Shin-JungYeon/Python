'''
Created on 2019. 7. 30.

@author: gd_4

test4.py : 간단한 암호문
'''
palpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
pnum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
calpha = ["`", "~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ":", ";", "<", "/", "?", ","]
cnum = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]

plain = input("문자를 입력하세요.")
result = ""
for i in range(0, len(plain)) :
    for d in range(0, len(palpha)) :
        if plain[i] == palpha[d] :
            result += calpha[d]
    for d in range(0, len(pnum)) :
        if plain[i] == pnum[d] :
            result += cnum[d]
print("암호문 : ", result)

cipher = result
result = ""
for i in range(0, len(cipher)) :
    for d in range(0, len(calpha)) :
        if cipher[i] == calpha[d] :
            result += palpha[d]
    for d in range(0, len(cnum)) :
        if cipher[i] == cnum[d] :
            result += pnum[d]
print("복호문 : ", result)