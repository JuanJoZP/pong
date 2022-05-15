import pygame
from config import WINDOWWIDTH


def draw_score(screen, p1, p2):
    """Draws the score in the main screen

    Parameters
    ----------
    screen: pygame.Surface
        the main surface to draw the score on
    p1: Paddle
        the paddle object corresponding to the player 1
    p2: Paddle
        the paddle object corresponding to the player 2
    """

    message = "{} {}  -  {} {}".format(p1[0], p1[1], p2[0], p2[1])

    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(message, True, "white", "black")

    textRect = text.get_rect()
    textRect.center = (WINDOWWIDTH // 2, 50)

    screen.blit(text, textRect)
