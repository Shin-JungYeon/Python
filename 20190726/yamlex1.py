'''
Created on 2019. 7. 26.

@author: gd_4

yamlex1.py
    json과 비슷한 문서 저장 방식. 2001년에 생성됨.
    json에 없는 간단한 기능들이 있음.
'''
import yaml  # pip3 install pyYAML
yaml_str = """
    Date : 2019-07-26
    PriceList :
        -
            item_id : 1000
            name : banana
            color : yellow
            price : 800
        -
            item_id : 1001
            name : orange
            color : orange
            price : 1000
        -
            item_id : 1002
            name : Apple
            color : red
            price : 500
"""
data = yaml.safe_load(yaml_str)
print("과일가격 일자 :", data["Date"])
for item in data["PriceList"] :
    print(item["name"], item["price"], "원")