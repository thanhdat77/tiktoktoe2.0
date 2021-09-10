import pygame
from tiktoktoe.constant import *
from tiktoktoe.board import Board



class Game:
    def __init__(self,win):
        self._init()
        self.win = win

    def _init(self):
        self.board = Board()
        self.turn = WHITE     
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    # def winner(self):
    #     return self.board.winner()
    def reset(self):
        self._init()

    def clickbutton(self, x, y):
        if x > 600 and y > HEIGHT and self.store[3]:
            self.turn = 4
            return True
        if x > 600 and y > 340:
            return True
        if x > 600 and y > 220:
            self.turn = 3
            return True
        if x > 600 and y > 0:
            self.turn = 1
            return True

    def click(self, x, y):
        if self.clickbutton(x, y):
            return True
        mourse_x, mourse_y = x // SIZE, y // SIZE

        if self.board[mourse_x][mourse_y] == 1 and self.turn == 4:
            self.board[mourse_x][mourse_y] = self.turn

        if self.board[mourse_x][mourse_y] == 2 and self.turn == 3:
            self.board[mourse_x][mourse_y] = self.turn

        if self.board[mourse_x][mourse_y] == -1:
            self.board[mourse_x][mourse_y] = self.turn
        self.store[self.turn] -= 1

    def winner(self):
        return self.board.winner()
