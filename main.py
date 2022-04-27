import pygame
import config as cf
from paddle import Paddle
from ball import Ball

pygame.init()

icon = pygame.image.load("icon.xcf")
pygame.display.set_icon(icon)
pygame.display.set_caption("PONG")

screen = pygame.display.set_mode(cf.SIZE)
screen.fill(cf.BLACK)


paddleplayer1 = Paddle()
paddleplayer1.rect.x = 10
paddleplayer1.rect.y = cf.WINDOWHEIGHT / 2 - cf.HEIGHTp / 2

paddleplayer2 = Paddle()
paddleplayer2.rect.x = cf.WINDOWWIDTH - cf.WIDTHp - 10
paddleplayer2.rect.y = cf.WINDOWHEIGHT / 2 - cf.HEIGHTp / 2

ball = Ball()


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

        # Points
        if ball.rect.x > cf.WINDOWWIDTH:
            paddleplayer1.scorePoint()
            ball.reset(1)

        if ball.rect.x < 0:
            paddleplayer2.scorePoint()
            ball.reset(0)

        screen.fill(cf.BLACK)
        paddleplayer1.draw(screen)
        paddleplayer2.draw(screen)
        ball.draw(screen)
        ball.move()
        ball.bounce(paddleplayer1, paddleplayer2)
        pygame.display.update()
        clock.tick(cf.FPS)


game()
pygame.quit()
