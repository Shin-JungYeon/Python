'''
Created on 2019. 7. 15.

@author: gd_4

mapex1.py : 리스트의 각각의 요소를 변경. (자바와는 다른 map임.)
'''
before = ["2019", "07", "15"]
print(type(before[0]))
after = list(map(int, before))  # 각각의 요소를 int 형태로 바꿔서 list로 저장.
print(type(after[0]))