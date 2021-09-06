import pygame
from tiktoktoe.constant import *
from tiktoktoe.board import Board


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tiktoktoe 2.0")
pygame.font.init()
WINNER_FONT = pygame.font.SysFont("comicsans", 70)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, YELLOW)
    WIN.blit(
        draw_text,
        (
            WIDTH / 2 - draw_text.get_width() / 2,
            HEIGHT / 2 - draw_text.get_height() / 2,
        ),
    )
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    run = True
    board = Board()

    while run:
        clock = pygame.time.Clock()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                mourse_x, mourse_y = pos[0] // SIZE, pos[1] // SIZE
                board.play(mourse_x, mourse_y)

        board.draw_board(WIN)
        if board.winer() != 0:
            winner_text = ""
            if board.winer() == 2:
                winner_text = "WHITE Wins!"

            if board.winer() == 1:
                winner_text = "Black Wins!"
            if winner_text != "":
                draw_winner(winner_text)
                break
    pygame.quit()


if __name__ == "__main__":
    main()
