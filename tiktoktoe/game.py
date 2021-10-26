import pygame
from .constant import WIDTH, HEIGHT, COLUMN, ROW, SIZE, TAN, GREEN, BLACK, WHITE, YELLOW

from tiktoktoe.board import Board

pygame.font.init()
WINNER_FONT = pygame.font.SysFont("comicsans", 100)


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
        self.board.draw(self.win)  # ve ban choi
        pygame.display.update()

    def winner(self):
        text = self.board.winner()  # ve text
        if text == 0:
            return False
        else:
            draw_text = WINNER_FONT.render(text, 1, YELLOW)
            self.win.blit(
                draw_text,
                (
                    WIDTH / 2 - draw_text.get_width() / 2,
                    HEIGHT / 2 - draw_text.get_height() / 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(2000)
            return True

    def reset(self):
        self._init()

    def get(self, row, col):  # lay vi tri ba hien tai
        text = self.board.get(row, col)
        if text != 0:
            return text
        else:
            return 0

    def clickleft(self, row, col):  # create small
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

    def clickright(self, row, col):  # create the big
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
