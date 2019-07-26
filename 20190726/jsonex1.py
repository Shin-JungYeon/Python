'''
Created on 2019. 7. 26.

@author: gd_4

jsonex1.py
'''
import json
import os.path, random
import urllib.request as req

url = "https://api.github.com/repositories"
savename = "repo.json"

if not os.path.exists(savename) :
    req.urlretrieve(url, savename)
    
items = json.load(open(savename, "r", encoding="utf-8"))  # json 파싱 결과 저장.
for item in items :  # items : [{}, {}, ...] -> item : {}
    print(item["name"], "-", item["owner"]["login"])

json.dump(items, open("json_output.json", "w", encoding="utf-8"))  # json 형태의 파일로 저장.