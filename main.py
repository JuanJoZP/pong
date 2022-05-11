import pygame
from paddle import Paddle
from ball import Ball
from config import (
    SIZE,
    WINDOWHEIGHT,
    WINDOWWIDTH,
    BLACK,
    WHITE,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    PADDLE_VELOCITY,
    PADDLE_XSPACING,
    FPS,
)

x=0
y=0
# window init
pygame.init()

icon = pygame.image.load("icon.xcf")
pygame.display.set_icon(icon)
pygame.display.set_caption("PONG")

screen = pygame.display.set_mode(SIZE)
screen.fill(BLACK)

clock = pygame.time.Clock()

# paddle and ball init
paddleplayer1 = Paddle(x)
paddleplayer1.rect.x = PADDLE_XSPACING
paddleplayer1.rect.y = WINDOWHEIGHT / 2 - PADDLE_HEIGHT / 2

paddleplayer2 = Paddle(y)
paddleplayer2.rect.x = WINDOWWIDTH - PADDLE_WIDTH - PADDLE_XSPACING
paddleplayer2.rect.y = WINDOWHEIGHT / 2 - PADDLE_HEIGHT / 2

"""Intento de texto"""
def puntaje():
    a=paddleplayer1.printPoint()
    b=paddleplayer2.printPoint()
    c="P1 {}  -  {} P2".format(a,b)
    pygame.display.set_caption('Show Text')
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    text = font.render(c, True, "white", "black")
    
    textRect = text.get_rect()
    
    textRect.center = (WINDOWWIDTH//2,50)

    screen.blit(text, textRect)
puntaje()

ball = Ball()


def game():
    x=0
    y=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

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
            y+=1

        if ball.rect.x < 0:
            paddleplayer2.scorePoint()
            ball.reset(0)
            x+=1

        if x==7 or y==7:
            break

        # elements display
        screen.fill(BLACK)
        paddleplayer1.draw(screen)
        paddleplayer2.draw(screen)
        ball.draw(screen)
        ball.bounce(paddleplayer1, paddleplayer2)
        puntaje()

        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()
