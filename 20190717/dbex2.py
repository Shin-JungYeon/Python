'''
Created on 2019. 7. 17.

@author: gd_4

dbex2.py : MariaDB와 연결.
'''
import pymysql  # 파이썬에는 MariaDB와 연결해주는 모듈 없음. 외부에 있는 것 가져와야 함. pip3 install pymysql -> python -m pip install --upgrade pip
conn = pymysql.connect(host="localhost", port=3306, user="model1", passwd="1234", db="model1", charset="utf8")

try :
    cur = conn.cursor()
    cur.execute("select * from item")
    for row in cur.fetchall() :
        print(row)
finally :
    cur.close()
    conn.close()