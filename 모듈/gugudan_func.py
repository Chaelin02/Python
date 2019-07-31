#p142 gugudan_func.py
def gugudan(n):
    print(n,"단을 출력합니다.")
    for i in range(1, 9+1):
        print(n, "X", i, "=", n*i)

if __name__ == '__main__':     #자기모듈 실행하면 실행되고, 다른데서 import 하면 실행안됨. 
        gugudan(3)