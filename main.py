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
pygame.font.init()
WINNER_FONT = pygame.font.SysFont("comicsans", 100)


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

        if game.winner() != 0:
            text = game.winner()
            draw_text = WINNER_FONT.render(text, 1, YELLOW)
            WIN.blit(
                draw_text,
                (
                    WIDTH / 2 - draw_text.get_width() / 2,
                    HEIGHT / 2 - draw_text.get_height() / 2,
                ),
            )
            pygame.display.update()
            # pygame.time.delay(3000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.clickleft(row, col)

                elif event.button == 3:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.clickright(row, col)

                elif event.button == 3 or event.button == 5:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.clickmid(row, col)

                print(game.turn_W, game.turn_B)
        game.update()
    pygame.quit()


if __name__ == "__main__":
    main()
