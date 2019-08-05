'''
Created on 2019. 8. 5.

@author: gd_4

learningex3.py : learningex1.py 를 pandas로 변경하기.
'''
import pandas as pd
from sklearn import svm, metrics

xor_input = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.loc[:, 0:1]
xor_label = xor_df.loc[:, 2]

clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 =", ac_score)

print("테스트 데이터를 평가하기.")
test = [[1, 1], [1, 0], [0, 1], [1, 1], [1, 0], [0, 0]]
pre = clf.predict(test)
ans = [0, 1, 1, 0, 1, 0]
ac_score = metrics.accuracy_score(ans, pre)
print("정답률 =", ac_score)