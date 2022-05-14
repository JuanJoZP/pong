import pygame
from game import game_1v1, game1vsCPU
from menu import menu
from config import BLACK, SIZE, FPS
from settings import settings

# window init
pygame.init()

icon = pygame.image.load("icon.xcf")
pygame.display.set_icon(icon)
pygame.display.set_caption("PONG")

screen = pygame.display.set_mode(SIZE)
screen.fill(BLACK)

clock = pygame.time.Clock()

state = {"n": 0}  # 0 for menu, 1 for 1vsCPU, 2 for 1vs1, 3 for settings


def main():
    global state
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while True:

        if state["n"] == 0:
            menu(screen, state)
        if state["n"] == 1:
            game1vsCPU(screen)
        if state["n"] == 2:
            game_1v1(screen)
        if state["n"] == 3:
            settings(screen, state)

        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
