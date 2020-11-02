words = ["apple", "piano", "jupyternotebook", "glass", "fish", "robot", "eyes", "sky", "time", "death"]
meaning = ["동그라며 먹는것", "소리가 나는 큰 물건", "인공지능 공부시 사용", "뭔가를 볼 때 사용", "음식 중 하나", "현재 많이 쓰이는 것", "뭔가를 비추는 창", "파란색이고 크다", "지나가면 돌아오지 않는 것", "두려워 하는 것"]
# 단어와 힌트 10개
from random import *

rand = randint(0, 9)
word = words[rand]
print("힌트 : " + meaning[rand])
print("글자 갯수 : " + str(len(word)))
print("< 한 글자씩 입력 >")
checkcount = len(word)
while True :
    num = int(input("글자 자리수 >> "))
    ch = input("입력할 글자 >> ")
    if checkcount == 1 :
        print("< 답을 맞추셨습니다 >")
        print("< 문자 : " + word + ' >')
    elif word[num-1] == ch :
        print("< 맞습니다 >")
        checkcount -= 1
    else :
        print("< 답이 아닙니다 >")
