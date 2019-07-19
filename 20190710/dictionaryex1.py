'''
Created on 2019. 7. 10.

@author: gd_4

dictionaryex1.py
'''
singer = {}  # dictionary 표현.
singer['이름'] = '트와이스'  # 인덱스 대신 key로 구분.
singer['구성원수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'signal'

for i in singer.keys() :  # 개선된 for문과 비슷.
    print("%s -> %s" % (i, singer[i]))
    
print(type(singer))
print(type(singer.keys()))
print(type(list(singer.keys())))