import pygame
import config as cf
from paddle import Paddle

pygame.init()

icon = pygame.image.load("icon.xcf")
pygame.display.set_icon(icon)
pygame.display.set_caption("PONG")

screen = pygame.display.set_mode(cf.SIZE)
screen.fill(cf.BLACK)


paddleplayer1 = Paddle()
paddleplayer1.rect.x = 10
paddleplayer1.rect.y = 0

paddleplayer2 = Paddle()
paddleplayer2.rect.x = cf.WINDOWWIDTH - cf.WIDTHp - 10
paddleplayer2.rect.y = 0

clock = pygame.time.Clock()

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleplayer1.moveUp(5)
        if keys[pygame.K_s]:
            paddleplayer1.moveDown(5)
        if keys[pygame.K_UP]:
            paddleplayer2.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleplayer2.moveDown(5)


        screen.fill(cf.BLACK)
        paddleplayer1.draw(screen)
        paddleplayer2.draw(screen)
        pygame.display.update()
        clock.tick(60)


game()
pygame.quit()
