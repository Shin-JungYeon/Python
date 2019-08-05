'''
Created on 2019. 8. 5.

@author: gd_4

learningex2.py : pandas를 이용하여 학습 데이터와 테스트 데이터 분류하기.
'''
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv("iris.csv")
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]  # 전체 데이터의 학습 데이터.
csv_label = csv["Name"]  # 전체 데이터의 결과값.

# train_test_split() : 읽어온 데이터를 메트릭스 형태로 저장하고 있다가 학습할 데이터와 학습 결과, 평가 데이터, 평가 결과 데이터로 분류.
#                      test_size=0.3 : 분류율 30%. 평가데이터(30), 학습데이터(70). 학습 데이터가 많을 수록 정답률 높아짐.
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label, test_size=0.2)

clf = svm.SVC()  # 머신 러닝 학습 객체.
clf.fit(train_data, train_label)  # 학습하기.
pre = clf.predict(test_data)  # 평가하기. 평가 결과를 가지고 있음.
ac_score = metrics.accuracy_score(test_label, pre)  # test_label : 제공된 정답. pre : 학습 결과값.
print("정답률 =", ac_score)