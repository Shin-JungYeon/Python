'''
Created on 2019. 7. 10.

@author: gd_4

dictionaryex1.py
'''
foods = {"떡볶이":"순대", "짜장면":"탕수육", "라면":"김치",
         "피자":"핫소스", "치킨":"맥주", "갈비":"냉면"}

for i in foods.keys() :
    print("%s -> %s" % (i, foods[i]))
    
while True :
    myfood = input(str(list(foods.keys())) + " 중 좋아하는 음식은? ")
    if myfood in foods :  # 입력 받은 값이 foods 에 존재?
        print("<%s> 궁합 음식은 <%s> 입니다." % (myfood, foods.get(myfood)))
    elif myfood == "끝" :
        for i in foods.keys() :
            print("%s -> %s" %(i, foods[i]), end=", ")
        break
    else :
        print("등록되어 있지 않은 음식입니다.")
        yn = input("좋아하는 음식으로 등록하시겠습니까? (y/n) ")
        if yn == 'y' :
            f = input("궁합음식을 입력하세요. ")
            foods[myfood] = f
        