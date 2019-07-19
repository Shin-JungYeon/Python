'''
Created on 2019. 7. 18.

@author: gd_4

dbex3.py : MariaDB에 레코드 등록하기.
'''
import pymysql
conn = pymysql.connect(host="localhost", port=3306, user="scott", passwd="tiger", db="bigdb", charset="utf8")

cur = conn.cursor()

cur.execute("drop table items;")
cur.execute("""
    create table items (
        item_id integer primary key auto_increment,
        name varchar(100),
        price integer
    );
""")

'''
auto_increment : MariaDB, mysql, mssql에서 사용 가능한 예약어.
                                      값을 자동으로 증가 시켜줌. primary key가 숫자인 경우에 사용 가능.
                 Oracle에는 없음. -> sequence(시퀀스)를 이용하여 사용 가능함.
'''

data = [("바나나", 3000), ("망고", 30000), ("사과", 10000)]
for d in data :  # d : ("바나나", 3000) 튜플 객체 하나.
    cur.execute("""
        insert into items (name, price) values (%s, %s);
    """, d)
    
conn.commit()

cur.execute("select * from items")
for row in cur.fetchall() :
    print(row[1], row[2])