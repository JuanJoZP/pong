import pygame
import config as cf

pygame.init()

icon = pygame.image.load("icon.xcf")
pygame.display.set_icon(icon)
pygame.display.set_caption("PONG")

screen = pygame.display.set_mode(cf.SIZE)
screen.fill(cf.BLACK)


def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.update()


game()
pygame.quit()
