'''
Created on 2019. 7. 26.

@author: gd_4

yamlex2.py : yaml 문서 저장하기.
'''
import yaml
customer = [
    {"name" : "InSeong", "age" : "24", "gender" : "man"},
    {"name" : "Kildong", "age" : "22", "gender" : "man"},
    {"name" : "ChunHang", "age" : "20", "gender" : "woman"},
    {"name" : "HangHan", "age" : "25", "gender" : "woman"}
]
yaml_str = yaml.dump(customer)  # yaml 형태의 문자열로 바꿔줌.
print(yaml_str)

data = yaml.safe_load(yaml_str)  # yaml을 파싱해서 저장.
for d in data :
    print(d["name"], d["age"], d["gender"])