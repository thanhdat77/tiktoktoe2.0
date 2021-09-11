import pygame
from .constant import WIDTH, HEIGHT, COLUMN, ROW, SIZE, TAN, GREEN, BLACK, WHITE

from tiktoktoe.board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.board = Board()
        self.color = WHITE
        self.turn_W = [3, 3, 3]
        self.turn_B = [3, 3, 3]

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def winner(self):
        text = self.board.winner()
        if text != 0:
            return text
        else:
            return 0
    def reset(self):
        self._init()

    def get(self, row, col):
        text = self.board.get(row, col)
        if text != 0:
            return text
        else:
            return 0

    def clickleft(self, row, col):
        if self.turn_W[0] > 0 and self.color == WHITE:
            if self.board.create_ox(row, col, self.color):
                self.turn_W[0] = self.turn_W[0] - 1
                self.chang_turn()
                return True
        if self.turn_B[0] > 0 and self.color == BLACK:
            if self.board.create_ox(row, col, self.color):
                self.turn_B[0] -= 1
                self.chang_turn()
                return True
        return False

    def clickmid(self, row, col):
        if self.turn_W[1] > 0 and self.color == WHITE:
            if self.board.create_queen(row, col, self.color):
                self.turn_W[1] -= 1
                self.chang_turn()
                return True
        if self.turn_B[1] > 0 and self.color == BLACK:
            if self.board.create_queen(row, col, self.color):
                self.turn_B[1] -= 1
                self.chang_turn()
                return True
        return False

    def clickright(self, row, col):
        if self.turn_W[2] > 0 and self.color == WHITE:
            if self.board.create_king(row, col, self.color):
                self.turn_W[2] -= 1
                self.chang_turn()
                return True
        if self.turn_B[2] > 0 and self.color == BLACK:
            if self.board.create_king(row, col, self.color):
                self.turn_B[2] -= 1
                self.chang_turn()
                return True
        return False

    def chang_turn(self):
        if self.color == WHITE:
            self.color = BLACK
        else:
            self.color = WHITE
