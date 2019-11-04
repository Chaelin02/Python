class TicTacToe:
    def __init__(self):
        self.board = [".",".",".",".",".",".",".",".","."]
        self.current_turn = "X"

    def set(self, row, col):                #X는 O로 O는 X로
#        if self.current_turn == "O":
#           self.current_turn = "X"
#       elif :
#           self.current_turn = "O"  아래 한줄과 같은소리임
        if self.get(row, col) == ".":
            self.current_turn = "X" if self.current_turn =="O" else "O"

            self.board[(row * 3) + col] = self.current_turn

    def get(self, row, col):                #row컬럼을 1차원적으로 그냥 바꿔주는 것
        return self.board[(row * 3) + col]

    def check_Winner(self):
        check = self.current_turn       #O체크 할건지 X체크할건지 
        for i in range(3):
            if self.get(i,0) == self.get(i,1) == self.get(i,2):
                # | 세로
                return check
            elif self.get()(0,i) == self.get(1,i) == self.get(2,i) == check:
                #  - 가로
                return check
                 #
            if self.get(0,0) == self.get(1,1) == self.get(2,2) == check:
                #
                    return check
            elif self.get(0,2) == self.get(1,1) == self.get(2,0) == check:
                return check

            if not "." in self.board:
                return "d" #비김



    def __str__(self):
        s = ""
        for i,v  in enumerate(self.board):   #enumerate값이랑 다가져오는 것
            s += v
            if i % 3 == 2:
                s += "\n"
        return s