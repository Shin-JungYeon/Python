'''
Created on 2019. 8. 5.

@author: gd_4

learningex1.py : 머신 러닝 소개. 사이킷 럿 툴 사용하기.
'''
from sklearn import svm  # pip3 install sklearn

xor_data = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]  # 같으면 0, 다르면 1
data = []  # 샘플 데이터.
label = []  # 결과값.
for row in xor_data :
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])  # 결과를 얻기 위한 데이터. 머신 러닝을 위한 학습 데이터.
    label.append(r)  # 결과값.
    
clf = svm.SVC()  # 머신러닝을 위한 준비.
clf.fit(data, label)  # 학습.

# 평가하기.
sample_data = [[1, 1], [1, 0], [0, 1], [1, 1], [1, 0], [0, 0]]
pre = clf.predict(sample_data)
ans = [0, 1, 1, 0, 1, 0]
print("예측 결과 :", pre)
ok = 0
total = 0
for idx, answer in enumerate(ans) :
    p = pre[idx]
    if p == answer :
        ok += 1
    total += 1
print("정답률 :", ok, "/", total, "=", ok/total)