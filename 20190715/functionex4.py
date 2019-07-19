'''
Created on 2019. 7. 15.

@author: gd_4

functionex4.py : 매개변수가 두 개 이상인 함수.

자바 :
    int paramMulti(int ... para) {  // 정수형 매개변수 갯수 상관없음. 가변 매개 변수. para : 배열로 전달.
        int result = 0;
        for(int p : para) {
            result += p;
        }
        return result;
    }
'''
def paramMulti(* para) :  # 매개변수 갯수의 제한 없음. 가변 매개변수.
    print(type(para))  # para : tuple로 전달
    result = 0;
    for num in para :
        result = result + num
    return result

hap = paramMulti()
print("paramMulti() = %d" % hap)

hap = paramMulti(10, 20)
print("paramMulti(10, 20) = %d" % hap)

hap = paramMulti(10, 20, 30)
print("paramMulti(10, 20, 30) = %d" % hap)

hap = paramMulti(10, 20, 30, 40, 50, 60, 70, 80, 90)
print("paramMulti(10, 20, 30, 40, 50, 60, 70, 80, 90) = %d" % hap)