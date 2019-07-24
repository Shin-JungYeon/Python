'''
Created on 2019. 7. 24.

@author: gd_4

plotex1.py : 그래프 예제
'''
import matplotlib.pyplot as plt  # 그래프를 그리기 위한 모듈. pip3 install ggplot

# 현재 사용 중인 폰트를 변경 : 한글 폰트로 설정해줘야 한글 부분 출력 됨.
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.style.use("ggplot")
customers = ["JAVA", "JSP", "SPRING", "HADOOP", "PYTHON"]
customers_index = range(len(customers))  # 그래프의(막대의) 갯수.
print(type(customers_index))  # range
print(customers_index)  # range(0, 5)
scores = [65, 90, 85, 60, 95]

fig = plt.figure()  # 그림판. 그래프를 그리기 위한 저장 공간.
ax1 = fig.add_subplot(1, 1, 1)  # 하나의 그림판에 여러개의 그림 그릴 수 있음. 영역 나눠주기. 1행 1열의 1번째 그래프 공간.
ax1.bar(customers_index, scores, align="center", color="darkblue")  # bar : 막대그래프.
ax1.xaxis.set_ticks_position("bottom")  # x축 설정.
ax1.yaxis.set_ticks_position("left")  # y축 설정.
plt.xticks(customers_index, customers, rotation=0, fontsize="small")  # 막대 그래프의 모양 설정.
plt.xlabel("과목")
plt.ylabel("점수")
plt.title("Class Score")
plt.savefig("bar_plot.png", dpi=400, bbox_inches="tight")  # fig 영역의 그래프를 파일로 저장. dpi : 해상도. bbox_inches=tight : 창 크기에 맞춰서.
plt.show()