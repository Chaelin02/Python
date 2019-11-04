from tkinter import *

window = Tk()
window.title("윈도창 연습")  # 캡션
window.geometry("760x500")  # 윈도우 창의 크기
window.resizable(width=TRUE, height=TRUE)  # 최대화 가능범위 둘 다 FALSE면 작동 불가

# 사진을 라벨로 출력

photo = PhotoImage(file="My_4.png")
label4 = Label(window, image=photo)

label4.pack()

window.mainloop()

