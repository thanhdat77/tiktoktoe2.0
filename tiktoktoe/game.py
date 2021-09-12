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
        self.turn = WHITE

    def play(self, row, col):
        if self.turn == WHITE:
            if self.board.click(row, col, self.turn):
                self.chang_turn()
        elif self.turn == BLACK:
            if self.board.click(row, col, self.turn):
                self.chang_turn()

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def winner(self):
        text = self.board.winner()
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

    def get(self, row, col):
        text = self.board.get(row, col)
        if text != 0:
            return text
        else:
            return 0

    def chang_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE
