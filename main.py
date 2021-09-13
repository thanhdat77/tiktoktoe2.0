import pygame
from pygame.constants import KSCAN_Z
from tiktoktoe.constant import (
    WIDTH,
    HEIGHT,
    COLUMN,
    ROW,
    SIZE,
    TAN,
    GREEN,
    BLACK,
    WHITE,
    YELLOW,
)
from tiktoktoe.game import Game


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tiktoktoe 2.0")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SIZE
    col = x // SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)
        if game.winner():
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.clickleft(row, col)

                elif event.button == 3:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.clickright(row, col)

                elif event.button == 2 or event.button == 5:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.clickmid(row, col)

        game.update()
    main()


if __name__ == "__main__":
    main()
