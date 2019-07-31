class Drink:
    _cups = ["레귤러", "점보"]
    _ices = [ "0%","50%","100%","150%" ]
    _sugars = [ "0%","50%","100%","150%" ]
  
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0  #0:레귤러 , 1:점보
        self.ice = 2 #0:0% , 1:50% , 2:100% 3:150%  #기본은 50%
        self.sugar = 2  #0:0% , 1:50% , 2:100% 3:150%
    def set_cup(self):
        self.cup = input("컵 사이즈를 선택하세요(0:레귤러 , 1:점보)")
        if self.cup == "":   #그냥 엔터치면 기본값 설정하자
            self.cup = 0
        else:
            self.cup = int(self.cup)
            # 점보를 선택하면 +500
        if self.cup == 1:
            self.price += 500
    def set_ice(self):
        self.ice = input("얼음량을 선택하세요(0:0%, 1:50%, 2:100%, 3:150%)")
        if self.ice == "":   #그냥 엔터치면 기본값 설정하자
            self.ice = 2
        else:
            self.ice = int(self.ice)
    def set_sugar(self):
        self.sugar = input("당도를 선택하세요(0:0%, 1:50%, 2:100%, 3:150%)")
        if self.sugar == "":
            self.sugar = 2
        else:
            self.sugar = int(self.sugar)
    def __str__(self):      #이름:sel.name\t컵사이즈:self.cut얼음량self.ice\t당도
        return "이름:"+self.name+"\t가격:" +str(self.price)+"\t컵사이즈:"+self._cups[self.cup]\
            +"\t얼음량:"+self._ices[self.ice]+"\t당도:"+self._sugars[self.sugar]
                #원래는 Drink._ices[self.ice]일케 하는게 맞음 
    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

