x = 3
while x < 6:
    print(x)
    x += 1
print("--------")
#echo = input()
#while echo != 'exit':
#   print(echo)
#    echo = input()
#print("--------")
# echo = input()
# while True:
    # if echo != 'exit':
    #     break
    # print(echo)
    # echo = input()

import random

def star(star, star_num, *star):
    str = star[0]
    for a in star:
        str = str+a
    print(str)
star("☆",3)
star("★",1,2,3)