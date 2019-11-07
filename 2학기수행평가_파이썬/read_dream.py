import os
from addr import Addr
from timequation import TimeQuation

class Read_Dream:
    def read_r(self):
            print("※(end누르면 종료)※ ")
            self.filename = input("불러올 파일명을 입력하세요:")

            if  self.filename == 'end':  # 반복문을 빠져나오는 조건문
                print("당신의 목표 불러오기를 종료합니다.\n")

            elif os.path.exists( self.filename):  # 파일 있을 때
                self.f = open( self.filename, "r", encoding="utf8")
                while True:
                    text = self.f.readline()
                    a = Addr()
                    a.array_1 = text
                    if not a.array_1:
                        break
                    print(a.array_1)
                t = TimeQuation()
                t.time_1
                self.f.close()

            else:
                print("해당파일이 존재하지않습니다... 다시입력해 주세요\n")

    # 목표를 적은 글과 해야할 일 3가지 적은 글 구분하기
    # 한 5초가 지나면 실천했냐고 물어보고 Y면 삭제하고 N 면 계속 남기기