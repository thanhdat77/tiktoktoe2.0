import pygame
from tiktoktoe.constant import *
from tiktoktoe.game import Game


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tiktoktoe 2.0")


def main():
    run = True
    game = Game()
    while run:
        clock = pygame.time.Clock()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y = pos
                if game.choose(x, y) != 0:
                    game.turn = game.choose(x, y)
                    print(game.turn)
                else:
                    mourse_x, mourse_y = pos[0] // SIZE, pos[1] // SIZE
                    game.play(mourse_x, mourse_y)
        game.draw_board(WIN)
        if game.draw_winner(WIN):
            run = False
    pygame.quit()


if __name__ == "__main__":
    main()
