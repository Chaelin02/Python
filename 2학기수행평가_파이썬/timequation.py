import threading
from addr import Addr

count = 0

class TimeQuation:

    def time_1(count):
        count += 1
        print(count)
        timer = threading.Timer(5.0, TimeQuation, args=[count])
        timer.start()
        if count == 5 :
            a = Addr()
            a.array_1()
            i = 0
            while i < len(a.todo):
                int
                print(a[i]+"를 하셨습니까?")
                answer3 = input("실천을 하셨다면 Y 못했다면 N 를 눌러주세요")
                if answer3 == 'Y':
                    del a[i] # 삭제
                elif answer3 == 'N':
                    continue