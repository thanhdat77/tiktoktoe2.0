import pygame
from tiktoktoe.constant import *


PADDING = SIZE // 2
RADIOUS = SIZE //4


class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 1
        self.change()

    def draw_board(self, win):
        win.fill(TAN)
        for row in range(ROW):
            for col in range(row % 2, COLUMN, 2):
                pygame.draw.rect(win, GREEN, (row * SIZE, col * SIZE, SIZE, SIZE))
        for row in range(ROW):
            for col in range(COLUMN):
                if self.board[col][row] == 1:
                    pygame.draw.circle(
                        win,
                        BLACK,
                        (col * SIZE + PADDING, row * SIZE + PADDING),
                        RADIOUS,
                    )
                if self.board[col][row] == 2:
                    pygame.draw.circle(
                        win,
                        WHITE,
                        (col * SIZE + PADDING, row * SIZE + PADDING),
                        RADIOUS,
                    )
        pygame.display.update()

    def play(self, mourse_x, mourse_y):
        self.board[mourse_x][mourse_y] = self.turn
        self.change()

    def change(self):
        if self.turn == 1:
            self.turn = 2
        else:self.turn = 1
        return self.turn
    def winer(self):
        for row in range(ROW):
            if self.board[row][0]==self.board[row][1]==self.board[row][2]:
                return self.board[row][0]          
        for col in range(COLUMN):
            if self.board[0][col]==self.board[1][col]==self.board[2][col]:
                return self.board[0][col]
        if self.board[0][0]==self.board[1][1]==self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2]==self.board[1][1]==self.board[2][0]:
            return self.board[1][1]    
