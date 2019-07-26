'''
Created on 2019. 7. 26.

@author: gd_4

xmlex1.py
'''
import os.path  # 현재 내가 가지고 있는 파일에 대한 정보 가지고 있음.
from bs4 import BeautifulSoup  # pip3 install beautifulsoup4  자바의 jsoup과 비슷.
import urllib.request as req  # 요청 정보. 요청할 수 있는 객체. url로부터 해당 정보를 가져올 수 있음.

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"
if not os.path.exists(savename) :  # savename 파일이 없는 경우에만
    req.urlretrieve(url, savename)  # url에 해당하는 페이지에 요청을해서, 요쳥의 결과 정보를 savename이라는 파일에 저장.

xml = open(savename, "r", encoding="utf-8").read()  # 파일을 읽어서 정보를 가지고만 있음.
soup = BeautifulSoup(xml, "html.parser")  # xml 문서의 최상단의 문서노드.
info = {}  # dictionary.

for location in soup.find_all("location") :  # soup 안에 있는 location 태그 전부 가져옴.
    name = location.find("city").string  # location 안에 있는 city 태그를 문자열로 바꿔서 name에 저장.
    weather = location.find("wf").string  # location 안에 있는 wf 태그...
    if not (weather in info) :
        info[weather] = []
    info[weather].append(name)
    
for weather in info.keys() :
    print("+", weather)
    for name in info[weather] :
        print("/ - ", name)