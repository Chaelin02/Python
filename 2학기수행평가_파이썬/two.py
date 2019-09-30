from Main import *
b001 = Book(title='사랑받는 방법')
b002 = Book(title='미움받을 용기')
b003 = Book(title='FBI의 심리학')
book_list = [b001, b002, b003]

library = Library(name='관산도서관')

for books in book_list:
    library.add_book(books)