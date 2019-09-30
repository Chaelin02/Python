# from tkinter import *
#
# window = Tk()
# window.title("윈도창 연습")  # 캡션
# window.geometry("760x500")  # 윈도우 창의 크기
# window.resizable(width=TRUE, height=TRUE)  # 최대화 가능범위 둘 다 FALSE면 작동 불가
#
# # 사진을 라벨로 출력
#
# photo = PhotoImage(file="My_4.png")
# label4 = Label(window, image=photo)
#
# label4.pack()
#
# window.mainloop()


class Library():
    """
    도서관
    """

    # 초기화
    def __init__(self, name):
        self.name = name
        self.book_list = []

    # 도서총판(Book) 에서 책을 인수
    def add_book(self, book):

        if book in self.book_list:
            print('이미 소장중인 도서입니다.')
        else:
            book.location = self.name
            book.is_borroweds = True
            self.book_list.append(book)
            print(f'{book.title} 이 도서관에 추가되었습니다.')

    # 책을 폐기
    def remove_book(self, book):
        if book in self.book_list:
            book.location = ''
            book.is_borrowed = '제고 없음'
            self.book_list.remove(book)
            print(f'{self.name}이 소장중인 도서목록 \n{self.book_list}')
        else:
            print('존재하지 않는 도서입니다.')

    # 정보
    @property
    def info(self):
        print(f'도서관: {self.name}\n장서목록: {[i.title for i in self.book_list]}')


class Book():
    """
    책 & 도서총판
    """

    # 초기화
    def __init__(self, title):
        self.title = title
        self.location = ''
        is_borroweds = ''

    # 대여 가능 여부
    @property
    def is_borrowed(self):
        if self.is_borroweds == False:
            return '대여중'
        elif self.is_borroweds == True:
            return '대여 가능'
        else:
            return '제고 없음'

	 # 정보
    @property
    def info(self):
        print(f'제목: {self.title}\n소재지: {self.location} \n대여여부: {self.is_borrowed}')

class User():
    """
    도서관 이용자
    """

    # 초기화
    def __init__(self, name):
        self.name = name
        self.book_list = []

    # 책 대여
    def borrow_book(self, library, book):
        if book in self.book_list:
            print('이미 소장중인 도서입니다.')
        else:
            library.book_list.remove(book)
            self.book_list.append(book)
            book.location = self.name
            book.is_borroweds = False
            print(f'{library.name} 에서 {book.title}을(를) 빌렸습니다.\n나의 소장 도서목록-\n{[i.title for i in self.book_list]}')

    # 책 반납
    def return_book(self, library, book):
        if book in self.book_list:
            library.book_list.append(book)
            self.book_list.remove(book)
            book.location = library.name
            book.is_borroweds = True
            print(f'{self.name} 이(가) {book.title}을(를) {library.name}에 반납했습니다.\n 나의 소장 도서목록-\n{[i.title for i in self.book_list]}')
        else:
            print('해당하는 도서가 없습니다.')

    # 정보
    @property
    def info(self):
        print(f'이름: {self.name}\n소장 도서목록-\n{[i.title for i in self.book_list]}')
