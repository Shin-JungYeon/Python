'''
Created on 2019. 7. 17.

@author: gd_4

dbex1.py : sqlite db 사용하기. 파이썬 자체에 데이터베이스를 가지고 있음.
'''
import sqlite3

dbpath = "test.sqlite"  # 데이터 베이스. 정보 저장.
conn = sqlite3.connect(dbpath)  # Connection 객체 생성.
cur = conn.cursor()  # 명령 전달 객체. 자바의 Statement 객체.
cur.executescript('''
    drop table if exists items;
    create table items (
        item_id integer primary key,
        name text unique,
        price integer
    );
    insert into items (name, price) values ("Apple", 800);
    insert into items (name, price) values ("Orange", 500);
    insert into items (name, price) values ("Banana", 300);
''')  # 명령어는 ; 으로 구분.
conn.commit()  # 실행 완성. <-> rollback
cur.execute("select * from items")
item_list = cur.fetchall()  # dbms의 실행 결과를 한 번에 리턴.
print(item_list)  # 전체는 리스트, 하나하나는 튜플.
for rt in item_list :
    print(rt)  # 튜플.