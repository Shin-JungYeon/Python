'''
Created on 2019. 7. 18.

@author: gd_4

soupex1.py : 크롤링 예제. 자바의 jsoup과 비슷함.
'''
from bs4 import BeautifulSoup  # pip3 install beautifulsoup4
import urllib.request as req  # 모듈의 이름을 req로 설정해서 사용.

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)
# soup : BeautifulSoup 객체.
# res : xml 문서의 내용이 저장되어 있는 객체. dom 형태의 객체.
# html.parser : html 형태로 인식할 수 있게 parser로 분석.
soup = BeautifulSoup(res, "html.parser")  # 객체 생성. 생성자 호출. 
title = soup.find("title").string  # 태그가 title인 부분을 가져와서 문자열로 저장.
wf = soup.find("wf").string  # 현재 가져온 wf 태그 안의 내용에 존재함. <![CDATA[...]] : CDATA 섹션. -> xml parser의 영향을 받지 않음.
print(title)
print(wf)