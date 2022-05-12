import pygame
from config import WINDOWWIDTH


def draw_score(screen, p1, p2):
    message = "P1 {}  -  {} P2".format(p1, p2)
    pygame.display.set_caption("Show Text")

    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(message, True, "white", "black")

    textRect = text.get_rect()
    textRect.center = (WINDOWWIDTH // 2, 50)

    screen.blit(text, textRect)
