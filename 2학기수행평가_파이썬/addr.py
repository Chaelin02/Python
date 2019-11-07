import array
class Addr:
    todo = []
    def add_b(self):
        answer2 = input("1.목표성공을 위해 할일 적기   2.해야할 일 추가")
        if answer2 == '1':
            self.filename = input("목표가 있는 파일명을 입력하세요:")
            self.f = open( self.filename, "a+", encoding="utf8")
            do = input("목표를 이루기 위하여 해야할 일 3가지를 사용하여 적어주세요(,로 구분)")
            print()
            self.f.write("해야 할 일 : ")
            self.f.write(do)
            self.f.close()
            print("파일이 저장되었습니다.\n")

        elif answer2 == '2':
            self.filename = input("목표가 있는 파일명을 입력하세요:")
            self.f = open(self.filename, "a+", encoding="utf8")
            do = input("추가할 내용을 적어주세요")
            self.f.write(","+do)
            self.f.close()
            print("파일이 저장되었습니다.\n")

    def array_1(self):
        while True:
            self.f = open(self.filename, "r", encoding="utf8")
            lines = self.f.readlines()
            for line in lines:
                item = line.split(",")
                todo = item[item.index("해야 할 일 : ") + 1]

        # result = line.split(",");
            #
            # line = self.f.readline();
# self.filename, "a+", encoding="utf8"



