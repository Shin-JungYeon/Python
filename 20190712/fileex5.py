'''
Created on 2019. 7. 12.

@author: gd_4

fileex5.py : 폴더 내의 파일 목록 조회하기.
'''
import os.path

print("파일 목록 보기 : os.walk 함수 사용.")
for dirName, subDirList, fnames in os.walk("c:\\temp1") :  # 하위 폴더가 있으면 그 폴더에 있는 파일도 읽어옴.
    for fname in fnames :
        print(os.path.join(dirName, fname))