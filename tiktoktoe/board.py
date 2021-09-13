from .constant import WIDTH, HEIGHT, COLUMN, ROW, SIZE, TAN, GREEN, BLACK, WHITE
from .ox import Ox
import pygame

PADDING = SIZE // 2
RADIOUS = SIZE // 4


class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        self.check_dia()
        self.check_straight()

    def get(self):
        # print(str(self.board))
        print("\n")
        print(self.turn_B, self.turn_W)

    def draw_board(self, win):
        win.fill(TAN)
        for row in range(ROW):
            for col in range(COLUMN):
                pygame.draw.rect(
                    win, GREEN, (row * SIZE + 10, col * SIZE, SIZE - 20, SIZE - 20)
                )
        pygame.display.update()

    def create_board(self):
        for row in range(ROW):
            self.board.append([])
            for col in range(COLUMN):
                self.board[row].append(0)
        pygame.display.update()

    def draw(self, win):
        self.draw_board(win)
        for row in range(ROW):
            for col in range(COLUMN):
                ox = self.board[row][col]
                if ox != 0:
                    ox.draw(win)

    def create_ox(self, row, col, color):
        if self.board[row][col] == 0:
            self.board[row][col] = Ox(row, col, color, 0)
            return True
        return False

    def create_queen(self, row, col, color):
        if self.board[row][col] == 0:
            self.board[row][col] = Ox(row, col, color, 1)
            return True
        elif self.board[row][col].get_king() == 0:
            self.board[row][col] = Ox(row, col, color, 1)
            return True
        return False

    def create_king(self, row, col, color):
        if self.board[row][col] == 0:
            self.board[row][col] = Ox(row, col, color, 2)
            return True
        elif (
            self.board[row][col].get_king() == 1 or self.board[row][col].get_king() == 0
        ):
            self.board[row][col] = Ox(row, col, color, 2)
            return True
        return False

    def check_straight(self):
        for row in range(ROW):
            if self.board[row][0] == self.board[row][1] == self.board[row][2]:
                if self.board[row][2] != 0:
                    return str(self.board[row][1])
        for col in range(COLUMN):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                if self.board[2][col] != 0:
                    return str(self.board[0][col])
        return 0

    def check_dia(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[2][2] != 0:
                return str(self.board[0][0])
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[2][0] != 0:
                return str(self.board[1][1])
        return 0

    def winner(self):

        if self.check_straight() == str(WHITE):
            return "WHITE WIN"
        if self.check_straight() == str(BLACK):
            return "BLACK WIN"
        if self.check_dia() == str(WHITE):
            return "WHITE WIN"
        if self.check_dia() == str(BLACK):
            return "BLACK WIN"
        return 0

    def get_king(self, row, col):
        if self.board[row][col] == 0:
            return 0
        return self.board[row][col].king()
