'''
Created on 2019. 7. 26.

@author: gd_4

jsonex2.py
    json 내용에서 과일의 가격을 화면에 출력하고, json_output2.json 파일에 저장.
'''
import json
price = {
    "data" : "2019-07-26",
    "price" : {
        "Apple" : 800,  # "Apple" : key, 800 : value
        "Orange" : 1000,
        "Banana" : 500
        }
    }
print("과일 가격 날짜 :", price["data"])
for p in price["price"].keys() :
    print("%s -> %d원" % (p, price["price"][p]))
json.dump(price, open("json_output2.json", "w", encoding="utf-8"))  # json 형태의 파일로 저장.