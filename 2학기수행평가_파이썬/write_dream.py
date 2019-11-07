import os
class Write_Dream:

    def write_w(self):

        print("※ ex)홍길동.txt 형식으로 작성해 주세요(end누르면 종료) ※")
        self.filename = input("파일명을 입력하세요 :")

        if  self.filename == 'end':  # 반복문을 빠져나오는 조건문
            print("one_List를 종료하겠습니다.\n")

        elif os.path.exists( self.filename):  # 파일 있을 때 에러발생
            print("이미 존재하는 파일입니다. 다시 입력해주세요.\n")

        else:  # 파일이 없으면 생성

            self.f = open( self.filename, "w", encoding="utf8")

            goal = input("본인의 목표를 작성해 주세요 : ")
            self.f.write("당신의 목표 : ")
            self.f.write(goal+"\n")
            self.f.close()

            print("파일이 생성되었습니다.\n")

            # v파일이 생성되면 아래 질문을 또 하고 거기에서 1,하면 작성하고 2.하면 불러올수 있게


