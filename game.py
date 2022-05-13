import pygame
from config import (
    SIZE,
    WINDOWHEIGHT,
    WINDOWWIDTH,
    BLACK,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    PADDLE_VELOCITY,
    PADDLE_XSPACING,
    FPS,
)
from paddle import Paddle
from ball import Ball
from score import draw_score

# paddle and ball init
paddleplayer1 = Paddle()
paddleplayer1.rect.x = PADDLE_XSPACING
paddleplayer1.rect.y = WINDOWHEIGHT / 2 - PADDLE_HEIGHT / 2

paddleplayer2 = Paddle()
paddleplayer2.rect.x = WINDOWWIDTH - PADDLE_WIDTH - PADDLE_XSPACING
paddleplayer2.rect.y = WINDOWHEIGHT / 2 - PADDLE_HEIGHT / 2

ball = Ball()


def game_1v1(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleplayer1.moveUp(PADDLE_VELOCITY)
    if keys[pygame.K_s]:
        paddleplayer1.moveDown(PADDLE_VELOCITY)
    if keys[pygame.K_UP]:
        paddleplayer2.moveUp(PADDLE_VELOCITY)
    if keys[pygame.K_DOWN]:
        paddleplayer2.moveDown(PADDLE_VELOCITY)
    if (not keys[pygame.K_w]) and (not keys[pygame.K_s]):
        paddleplayer1.action = 0
    if (not keys[pygame.K_UP]) and (not keys[pygame.K_DOWN]):
        paddleplayer2.action = 0

    # points and reset
    if ball.rect.x > WINDOWWIDTH:
        paddleplayer1.scorePoint()
        ball.reset(1)

    if ball.rect.x < 0:
        paddleplayer2.scorePoint()
        ball.reset(0)

    if paddleplayer1.getPoints() == 7 or paddleplayer2.getPoints() == 7:  # TEMPORAL
        return

    # elements display
    screen.fill(BLACK)
    paddleplayer1.draw(screen)
    paddleplayer2.draw(screen)
    ball.draw(screen)
    ball.bounce(paddleplayer1, paddleplayer2)
    draw_score(screen, paddleplayer1.getPoints(), paddleplayer2.getPoints())
