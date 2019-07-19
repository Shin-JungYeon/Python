'''
Created on 2019. 7. 10.

@author: gd_4

exam1.py : 나라와 수도를 등록하고 화면에 나라 이름을 입력받아 해당 나라의 수도를 출력.
    등록된 나라가 아니면 수도 등록하기.
    나라 입력 시 '종료' 입력되면 프로그램 종료.
    종료 시 등록된 모른 나라와 수도 정보 화면에 출력하기.
'''
contries = {"대한민국":"서울", "프랑스":"파리", "독일":"베를린",
            "일본":"도쿄", "미국":"워싱턴", "중국":"베이징"}
contries.pop("일본")  # 지우기 메서드.

while True :
    mycontry = input(str(list(contries.keys())) + " 중 수도가 궁금한 나라는? ")
    if mycontry in contries :
        print("<%s>의 수도는 <%s> 입니다." % (mycontry, contries.get(mycontry)))
    elif mycontry == "끝" :
        for i in contries.keys() :
            print("%s -> %s" % (i, contries[i]), end=", ")
        break
    else :
        print("수도가 등록되어 있지 않은 나라입니다.")
        yn = input("나라를 등록하시겠습니까? (y/n) ")
        if yn == 'y' :
            c = input("수도를 입력하세요. ")
            contries[mycontry] = c
            