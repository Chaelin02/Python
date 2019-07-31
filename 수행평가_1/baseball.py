#야구게임  strickm 는 질;,ball은 숫자
#세자리 중복 없는 임의의수 만들자
#무한반복
#사용자 입력을 받자 - input()
#strick, ball 판정하자
#사용자 입력한것, strick, ball 출력하자 - print()
#임의의수랑 사용자 입력한게 같으면 HIT, break  - if
#computer =str(random.randrange(100,999+1))

# r0 = random.randrange(1,9+1)  #randrange은 random의 함수
# r0 = str(r0)
# r1 = random.randrange(1,9+1) 
# r1 = str(r1)
# r2 = random.randrange(1,9+1)  
# r2 = str(r2)
# computer = r0+r1+r2


# random.shuffle(list(range(1,9+1)))
# ' '.join(str(i) for i in l[:3])

# a = ""
# for i in l[:3]:
#     a+=str(i)

import random
l = random.sample(range(1,9+1), 3)
computer = ' '.join(str(i) for i in l)

computer = "851"
while True:
    player = input("숫자 세자리 맞춰봐: ")
    strick = 0
    ball = 0
    #strick, ball 판정하자
    for i in range(len(computer)):
        for j in range(len(player)):
            if computer[i] == player[j]:  #글자가 같은지
                if i==j: #자릿수가 같은지
                    strick += 1
                else:
                    ball += 1
    print("{}\tstrick:{}\tball:{}".format(player,strick,ball))  
   # print(player,"strick : ",strick,"ball : ",ball)
    if computer == player:
        print("HIT")
        break