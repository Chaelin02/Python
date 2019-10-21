from order import Order
from file_manager import FileManager

file_manager = FileManager("hisotry.bin")

#history 있으면 내역 보여주자
history = []
try:
    history = file_manager.load()
    sum = 0
    for d in history:
        print(d)
        sum += d.price
    print("여태껏 아마스빈에 퍼부은 내 돈 : "+str(sum) + "원")
except FileNotFoundError:
    print("내역이 없습니다.")
print("---------------------------------------------")

o = Order()
o.order_drink()

#history에 저장하자  사용자한테 묻지 않고 저장함
file_manager.save(history + o.order_menu)

