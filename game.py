# this project is for me to practise functional programming
# This is SUPER tic-tac-toe: https://www.youtube.com/shorts/_Na3a1ZrX7c
# SqN denotes that the number of squares contained within is 9^N

from CONST import *


# must be called every time a victory is possible.
def checkVictory(board, y, x, turn):
    curr_v = curr_h = 0
    for i in range(3):
        curr_v += board[i][x].taken_by == turn
        curr_h += board[y][i].taken_by == turn
    print(curr_v, curr_h)
    if curr_v == 3 or curr_h == 3:
        return True
    for line in diagonals:
        curr = 0
        for a, b in line:
            curr += board[a][b].taken_by == turn
        if curr == 3:
            return True
    return False


class Game:
    def __init__(self):
        self.turn = "X"
        self.board = [[Sq1() for _ in range(3)] for _ in range(3)]
        self.squares_taken = 0
        self.chosen_square = None
        self.move_order = []

    def make_move(self, y, x, i, j):
        self.move_order.append(((y, x), (i, j), self.turn, self.chosen_square))
        cVic, square = self.board[y][x].make_move(i, j, self.turn)

        if self.board[y][x].completed:
            self.squares_taken += 1

        ni, nj = square
        self.chosen_square = None if self.board[ni][nj].completed else square

        if checkVictory(self.board, y, x, self.turn):
            return "WINNER IS " + self.turn + "!"
        self.turn = "O" if self.turn == "X" else "X"
        return False

    def undo(self):
        if not self.move_order:
            return
        move = self.move_order.pop(-1)
        (y, x), (i, j), turn, cs = move

        self.board[y][x].board[i][j].taken_by = None
        self.board[y][x].completed = False
        self.board[y][x].taken_by = None
        self.board[y][x].squares_taken -= 1
        self.chosen_square = cs
        self.turn = turn

    def print_game(self):
        for row in self.board:
            for i in range(3):
                for square in row:
                    print(" ", end="")
                    for tiny_square in square.board[i]:
                        if tiny_square.taken_by:
                            print(tiny_square.taken_by, end="")
                        else:
                            print("_", end="")
                    print(" ", end="")
                print()
            print()


class Sq1:
    def __init__(self):
        self.completed = False
        self.taken_by = None
        self.squares_taken = 0
        self.board = [[Sq0() for _ in range(3)] for _ in range(3)]

    def make_move(self, y, x, turn):
        self.board[y][x].take(turn)
        self.squares_taken += 1
        cVic = checkVictory(self.board, y, x, turn)
        if cVic:
            self.completed = True
            self.taken_by = turn
        elif self.squares_taken == 9:
            self.completed = True
        return cVic, (y, x)


# It really is unnecessary to make Sq0 a class. Could just be three symbols. BUT
# I am practising functional programming, and it looks pretty so >:(
# ALSO it makes it so that I can use checkVictory for both the mega square and the normal squares!
class Sq0:
    def __init__(self):
        self.taken_by = None

    def take(self, taker):
        self.taken_by = taker

