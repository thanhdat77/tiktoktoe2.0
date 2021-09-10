import pygame
from .constant import WIDTH, HEIGHT, COLUMN, ROW, SIZE, TAN, GREEN, BLACK, WHITE

from tiktoktoe.board import Board



class Game:
    def __init__(self,win):
        self._init()
        self.win = win

    def _init(self):
        self.board = Board()
        self.color = WHITE
        self.turn_W = 3
        self.turn_B = 3
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()
    
    def winner(self):
        return self.board.winner() 
    
    def reset(self):
        self._init()

    def winner(self):
        return self.board.winner()
        
    def get(self,row,col):
        return self.board.get(row,col)

    def click(self,row,col):
        if  self.turn_W > 0 and self.color==WHITE:
            self.board.create_ox(row,col,self.color)
            self.turn_W -= 1
            self.chang_turn()
            return True
        if  self.turn_B > 0 and self.color==BLACK:
            self.board.create_ox(row,col,self.color)
            self.turn_B -= 1
            self.chang_turn()
            return True
        return False
    def chang_turn(self):
        if self.color == WHITE:
            self.color = BLACK
        else: self.color = WHITE

