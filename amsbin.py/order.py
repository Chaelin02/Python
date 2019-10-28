from drink import Drink
from coffee import Coffee
from bubbletea import Bubbletea

#import ...


class Order:
   # _drinks = [Coffee("아메리카노",1800),Bubbletea("딸기요거트",3500)] #0을누르면 커피객체 생성, 1번을 누르면 버블티 객체 생성
    def __init__(self):
        self.order_menu = []   #주문한 음식을 담는곳

    def show_menu(self):
        print("0:아메리카노 1800원, 1:딸기요거트 3500원")

    def order_drink(self):
        #반복↓
        while True:
            #show menu
            self.show_menu()
            #주문받자. 음료선택하자
            order = input("무엇을 고르시겠습니까?")     
            if order == "":
                break
            if int(order) ==0:
                drink = Coffee("아메리카노", 1800)
            elif int(order) == 1:
                drink =Bubbletea("딸기요거트", 3500)
           # drink = Order._drinks[int(order)]   
            #3.음료옵션선택하자
            drink.order() 
            #1번
            # Drink  drink = Bubbletea("딸기요거트",3500)자바는 이렇게 .    
            self.order_menu.append(drink)
            #4.주문한 음료 내용 보여주자
        #반복↑
        for d in self.order_menu:
            print(d)
        #5.합계 금액 보여주자 
        print("총 금액: "+str(self.sum_price())+"원")

    def sum_price(self):
        sum = 0
        for d in self.order_menu:
            sum += d.price

        return sum
