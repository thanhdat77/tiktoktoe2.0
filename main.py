import pygame
from tiktoktoe.constant import WIDTH, HEIGHT, COLUMN, ROW, SIZE, TAN, GREEN, BLACK, WHITE
from tiktoktoe.game import Game


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tiktoktoe 2.0")
pygame.display.init()


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
            if game.winner() == str(WHITE):
                print('WHITE Thang')
            else:print('Black thang')
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.click(row,col)
                print(game.get(row,col))
        game.update()
    pygame.quit()


if __name__ == "__main__":
    main()
