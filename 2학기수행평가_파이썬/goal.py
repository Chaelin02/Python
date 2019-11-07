import os
from read_dream import Read_Dream
from write_dream import Write_Dream
from addr import Addr
class Goal:
    def goal_Start(self):# 반복↓
        while True:
            answer = input("1.새로운 목표작성하기  2.내 목표 불러오기 3.할 일적기 (엔터치면 종료)\n")

            if answer == "":  # 사용자가 엔터를 치면 끝난다.
                break
            elif answer == '1':  # 1을 누르면 read_dream.py를 불러와서 실행
                w = Write_Dream()
                w.write_w()
            elif answer == '2':  # 2을 누르면 write_dream.py를 불러와서 실행
                r=Read_Dream()
                r.read_r()
            elif answer == '3':
                a = Addr()
                a.add_b()
