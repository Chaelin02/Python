from school import School
from office import Office
from public import Public 
from life import Life

class Order:
    # def menu(self):
    def order_question(self):
            #반복↓
        
        while True:
            #show menu
            # self.menu()
              
            print("1.학교에서\
                2.회사에서\
                3.공공장소에서\
                4.일상생활에서 ") 

            User_S = input("알고싶은 문장의 번호를 선택하세요") 
            
            if User_S == "": #사용자가 엔터를 치면 끝난다.
                break
            elif User_S == '1':   #1을 누르면 school.py를 불러와서 실행
                s = School()
                s.run(User_S)
            elif User_S == '2': #2을 누르면 school.py를 불러와서 실행
                o = Office()
                o.run(User_S)
            elif User_S == '3':     #3을 누르면 school.py를 불러와서 실행
                p = Public()
                p.run(User_S)
            elif User_S == '4':         #4을 누르면 school.py를 불러와서 실행
                l = Life()
                l.run(User_S)
                    
        