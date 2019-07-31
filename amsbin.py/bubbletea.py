import drink    #소문자에서 대문자를 가져오겠다. #겹치는 것을 모르면 일케쓰고 알고있으면 from으로.

class Bubbletea(drink.Drink):
    _pearls = ["타피오카","코코","젤리","알로에"]   #_를 붙이는 이유는 감추고싶은 변수여서
    def __init__(self, name, price):
        super().__init__(name,price)
        self.pearl = 0  #0:타피오카 1:코코 2:젤리 3:알로에

    def set_pearl(self):
        self.pearl = input("펄을 선택하세요(0:타피오카 1:코코 2:젤리 3:알로에)")
        if self.pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(self.pearl)

    def __str__(self):
       return super().__str__() + "\t펄:"+self._pearls[self.pearl]

    def order(self):
        # self.set_cup()
        # self.set_ice()
        # self.set_sugar()
        super().order()
        self.set_pearl()
