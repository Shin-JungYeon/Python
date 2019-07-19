'''
Created on 2019. 7. 18.

@author: gd_4

soupex2.py : 내가 만든 html 파일을 soup을 이용하여 분석하기.
'''
from bs4 import BeautifulSoup

fp = open("books.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q : print(q, ":", soup.select_one(q).string)  # 출력 함수 설정.

sel("#nu")  # id 속성의 값이 nu인 태그의 정보 출력.
sel("li#nu")  # li 태그 중 id 속성의 값이 nu.
sel("ul > li#nu")  # ul 바로 아래(하위)의 li 태그 중 id 속성의 값이 nu.
sel("#bible #nu")  # id 속성의 값이 bible인 태그의 하위(자손) 태그 중 id 속성의 값이 nu.
sel("#bible > #nu")  # id 속성의 값이 bible인 태그의 바로 하위(자식) 태그 중 id 속성의 값이 nu.
sel("ul#bible > li#nu")
sel("li[id='nu']")
sel("li:nth-of-type(4)")  # li 태그 중 4번 째 태그.

print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)