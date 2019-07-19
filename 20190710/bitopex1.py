'''
Created on 2019. 7. 10.

@author: gd_4

bitopex1.py : 비트 연산자 예제
'''
a = ord('A')  # 아스키 코드값 리턴.
print(a)

mask = 0x0F  # 16진수 F, 10진수 15, 2진수 00001111

print("%X & %X = %X" % (a, mask, a&mask))
'''
    a : 16진수 41, 2진수 01000001
    m :      0F,     00001111
    -------------------------
    & :              00000001
'''

print("%X | %X = %X" % (a, mask, a|mask))
'''
    a : 16진수 41, 2진수 01000001
    m :      0F,     00001111
    -------------------------
    | :              01001111
'''

print("%X ^ %X = %X" % (a, mask, a^mask))
'''
    a : 16진수 41, 2진수 01000001
    m :      0F,     00001111
    -------------------------
    ^ :              01001110
'''
print()

a = 100
result = 0
for i in range(1, 5) :
    result = a << i
    print("%d << %d = %d" % (a, i, result))  # 2배 효과
print()
for i in range(1, 5) :
    result = a >> i
    print("%d >> %d = %d" % (a, i, result))  # 1/2배 효과
