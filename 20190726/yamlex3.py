'''
Created on 2019. 7. 26.

@author: gd_4

yamlex3.py : yaml alias 설정하기.
'''
import yaml
yaml_str = """
    # 문서 안에 주석도 들어올 수 있음.
    # 정의
    color_def :
        - &color1 "#FF0000"
        - &color2 "#00FF00"
        - &color3 "#0000FF"
    # 별칭 정하기
    color :
        title : *color1
        body : *color2
        link : *color3
"""
data = yaml.safe_load(yaml_str)
print("title=", data["color"]["title"])
print("body=", data["color"]["body"])
print("link=", data["color"]["link"])