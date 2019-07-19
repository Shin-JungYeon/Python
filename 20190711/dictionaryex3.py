'''
Created on 2019. 7. 11.

@author: gd_4

dictionaryex3.py
'''
import operator  # 기본 제공 모듈.
tranDic, tranList = {}, []  # {} : dictionary, [] : list, () : tuple(변경 불가 list)
tranDic = {"Thomas":"토마스", "Edward":"에드워드", "Henry":"헨리", 
           "Gothen":"고든", "James":"제임스"}
# tranDic.items() : (key, value) 쌍인 객체들.
# sorted(정렬 대상, 정렬 기준 데이터 설정) : 정렬.
# key=operator.itemgetter(1) : 두 번 째 객체(value) 기준으로 정렬.
# key=operator.itemgetter(0) : 첫 번 째 객체(key) 기준으로 정렬.
tranList = sorted(tranDic.items(), key=operator.itemgetter(1))
print(tranList)
print(type(tranList))  # list
tranList = tranDic.items()
print(tranList)
print(type(tranList))  # dict_items -> 자료형이 계속해서 바뀜.