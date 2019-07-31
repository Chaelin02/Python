#p142 gugudan_main.py
import gugudan_func

for i in range(2 , 9+1):
    print("="*20)
    gugudan_func.gugudan(i)
#    gugudan_func(모듈이름)이 나와야함 
    #3단먼저 출력이 되는 이유는 gugudan_func 에서 먼저 가져왔기 때무넹 
    # 그다음 2단이 출력.