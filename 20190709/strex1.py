'''
Created on 2019. 7. 9.

@author: gd_4

strex1.py : 문자열 값 출력하기. 문자열은 문자의 배열로 인식.
'''
print("안녕하세요")
print("안녕하세요"[0])
print("안녕하세요"[4], "안녕하세요"[-1])  # 뒤에서부터 인덱스 셀 때는 음수로 1부터 시작.
print("안녕하세요"[3], "안녕하세요"[-2])
print("안녕하세요"[1:3])  # 1번 인덱스부터 2(3-1)번 인덱스까지 부분 문자열 가져옴.
print("안녕하세요"[:2])  # 맨 앞이 0이면 생략 가능.
print("안녕하세요"[2:])  # 마지막 인덱스를 생략하면 끝까지 가져옴.
print()

s = "안녕하세요"
print(type(s))  # str
print("s 문자열의 길이 :", len(s))
print(type(len(s)))  # int

num = 10
print(type(num))  # int

num = 10.5
print(type(num))  # float. 입력된 값에 따라 자료형 변함.

print()

# 배열 : list 자료형. 순서를 유지.
arr = [10, 20, 30, 40, 50, 60, 70]
print(type(arr))
print(arr[0])  # 인덱스로 값을 가져올 수 있음. 단순히 값만 가져옴.
print(arr[:1])  # list로 가져옴. sublist의 형태.

# 30부터 50까지의 값만 출력
print(arr[2:5])
print(arr[::2])  # 인덱스를 2씩 건너뛰어서 가져옴.
print(arr[::-2])  # 인덱스를 2씩 건너뛰어서 뒤에서부터 가져옴.