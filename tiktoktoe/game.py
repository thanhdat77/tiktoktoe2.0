import pygame
from tiktoktoe.constant import *


PADDING = SIZE // 2
RADIOUS = SIZE // 4


pygame.font.init()
WINNER_FONT = pygame.font.SysFont("comicsans", 70)


class Game:
    def __init__(self):
        self.board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.turn = 0
        self.store = {"1": 3, "2": 3, "3": 3, "4": 3}
        self.winner_text = ""
        self.winer()

    def draw_board(self, win):
        win.fill(TAN)
        for row in range(ROW):
            for col in range(COLUMN):
                if self.board[row][col] == -1:
                    pygame.draw.rect(
                        win, GREEN, (row * SIZE, col * SIZE, SIZE - 20, SIZE - 20)
                    )
                if self.board[row][col] == 3:
                    pygame.draw.rect(
                        win, BLACK, (row * SIZE, col * SIZE, SIZE - 20, SIZE - 20)
                    )
                    win.blit(DRA180, (row * SIZE, col * SIZE))
                if self.board[row][col] == 4:
                    pygame.draw.rect(
                        win, WHITE, (row * SIZE, col * SIZE, SIZE - 20, SIZE - 20)
                    )
                if self.board[row][col] == 1:
                    pygame.draw.circle(
                        win,
                        BLACK,
                        (row * SIZE + PADDING, col * SIZE + PADDING),
                        RADIOUS,
                    )
                    win.blit(EGG180, (row * SIZE, col * SIZE))

                if self.board[row][col] == 2:
                    pygame.draw.circle(
                        win,
                        WHITE,
                        (row * SIZE + PADDING, col * SIZE + PADDING),
                        RADIOUS,
                    )
        pygame.draw.rect(win, WHITE, (600, 100, 100, 100))  # button
        win.blit(EGG100, (600, 100))
        pygame.draw.rect(win, WHITE, (600, 220, 100, 100))
        win.blit(DRA100, (600, 220))
        pygame.draw.rect(win, WHITE, (600, 340, 100, 100))
        pygame.draw.rect(win, WHITE, (600, 460, 100, 100))

        pygame.display.update()

    def play(self, mourse_x, mourse_y):
        if self.board[mourse_x][mourse_y] == -1 and self.store[str(self.turn)] != 0:
            self.board[mourse_x][mourse_y] = self.turn
            self.store[str(self.turn)] -= 1
        if (
            self.board[mourse_x][mourse_y] == 1
            and self.turn == 4
            and self.store[str(self.turn)] != 0
        ):
            self.board[mourse_x][mourse_y] = self.turn
            self.store[str(self.turn)] -= 1
        if (
            self.board[mourse_x][mourse_y] == 2
            and self.turn == 3
            and self.store[str(self.turn)] != 0
        ):
            self.board[mourse_x][mourse_y] = self.turn
            self.store[str(self.turn)] -= 1

    def winer(self):
        for row in range(ROW):
            if (
                self.board[row][0] % 2
                == self.board[row][1] % 2
                == self.board[row][2] % 2
            ):
                return self.board[row][0]
        for col in range(COLUMN):
            if (
                self.board[0][col] % 2
                == self.board[1][col] % 2
                == self.board[2][col] % 2
            ):
                return self.board[0][col]
        if self.board[0][0] % 2 == self.board[1][1] % 2 == self.board[2][2] % 2:
            return self.board[0][0]
        if self.board[0][2] % 2 == self.board[1][1] % 2 == self.board[2][0] % 2:
            return self.board[1][1]
        return 0

    def draw_winner(self, win):
        if self.winer() != 0:
            if self.winer() == 2 or self.winer() == 4:
                self.winner_text = "WHITE Wins!"
            if self.winer() == 1 or self.winer() == 3:
                self.winner_text = "Black Wins!"
            draw_text = WINNER_FONT.render(self.winner_text, 1, YELLOW)
            win.blit(
                draw_text,
                (
                    WIDTH // 2 - draw_text.get_width() // 2,
                    HEIGHT // 2 - draw_text.get_height() // 2,
                ),
            )
            pygame.display.update()
            pygame.time.delay(2000)
            return True
        return False

    def choose(self, x, y):
        if x > 600 and y > 460:
            return 4
        if x > 600 and y > 340:
            return 2
        if x > 600 and y > 220:
            return 3
        if x > 600 and y > 100:
            return 1
        return 0
