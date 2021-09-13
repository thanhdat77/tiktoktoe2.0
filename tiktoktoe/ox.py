import pygame
from .constant import WIDTH, HEIGHT, COLUMN, ROW, SIZE, TAN, GREEN, BLACK, WHITE


class Ox:
    def __init__(self, row, col, color, king):
        self.color = color
        self.king = king
        self.row = row
        self.col = col
        self.calc_pos()
        self.x
        self.y

    def calc_pos(self):
        self.x = SIZE * self.col + SIZE // 2
        self.y = SIZE * self.row + SIZE // 2

    def draw(self, win):
        radius = SIZE // 3
        if self.king == 0:
            pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        elif self.king == 1:
            pygame.draw.rect(
                win,
                self.color,
                (self.col * SIZE + 30, self.row * SIZE + 25, SIZE - 60, SIZE - 60),
            )
        elif self.king == 2:
            pygame.draw.rect(
                win,
                self.color,
                (self.col * SIZE + 10, self.row * SIZE, SIZE - 20, SIZE - 20),
            )

    def get_king(self):
        return self.king

    def __repr__(self):
        return str(self.color)

    def __str__(self):
        return str(self.color)

    def __eq__(self, other):
        if isinstance(other, Ox):
            if self.color == other.color:
                return True
            return False
