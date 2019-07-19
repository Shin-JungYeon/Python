'''
Created on 2019. 7. 16.

@author: gd_4

yieldex1.py : 함수 실행 중에 함수를 호출한 곳에 값을 전달해 줄 수 있음.
'''
# function
def genData(num) :
    for i in range(10, num+10) :
        yield i  # 중간에 값 전달. 리턴은 함수의 모든 내용이 실행 된 후 최종값만 전달.
        print(i, "값 전달")
        
# main
for data in genData(5) :
    print("main 전달 받은 값 :", data)
    
datalist = list(genData(5))
print(datalist)