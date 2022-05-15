import pygame
from config import (
    SIZE,
    WINDOWHEIGHT,
    WINDOWWIDTH,
    BLACK,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    settings,
    PADDLE_XSPACING,
    FPS,
    WHITE,
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

pygame.init()
counter = 0
timer = f"{counter}"
font = pygame.font.SysFont("inkfree", 25)


def game_1v1(screen, state):
    global timer
    global counter
    timer_s = state["data"]["timer_s"]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.USEREVENT:
            counter += 1
            timer = (
                f"{int(timer_s) - counter}"
                if int(timer_s) - counter > 0
                else "End of the Game"
            )

    # key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleplayer1.moveUp(settings["PADDLE_VELOCITY"])
    if keys[pygame.K_s]:
        paddleplayer1.moveDown(settings["PADDLE_VELOCITY"])
    if keys[pygame.K_UP]:
        paddleplayer2.moveUp(settings["PADDLE_VELOCITY"])
    if keys[pygame.K_DOWN]:
        paddleplayer2.moveDown(settings["PADDLE_VELOCITY"])
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

    # game end
    if (
        int(timer_s) - counter <= 0
        or paddleplayer1.getPoints() >= int(state["data"]["max_score"])
        or paddleplayer2.getPoints() >= int(state["data"]["max_score"])
    ):
        p1_name = state["data"]["p1_name"]
        p2_name = state["data"]["p2_name"]
        winner = ""
        if paddleplayer1.getPoints() > paddleplayer2.getPoints():
            winner = p1_name
        elif paddleplayer1.getPoints() < paddleplayer2.getPoints():
            winner = p2_name
        else:
            winner = "draw"

        state["data"]["winner"] = winner
        state["n"] = 6  # go to end screen

    # elements display
    screen.fill(BLACK)
    paddleplayer1.draw(screen)
    paddleplayer2.draw(screen)
    ball.draw(screen)
    ball.bounce(paddleplayer1, paddleplayer2)
    draw_score(
        screen,
        (state["data"]["p1_name"], paddleplayer1.getPoints()),
        (state["data"]["p2_name"], paddleplayer2.getPoints()),
    )
    screen.blit(font.render(timer, True, (WHITE)), (465, 10))


def game1vsCPU(screen, state):
    global timer
    global counter
    timer_s = state["data"]["timer_s"]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.USEREVENT:
            counter += 1
            timer = (
                f"{int(timer_s) - counter}"
                if int(timer_s) - counter > 0
                else "End of the Game"
            )

    # key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleplayer1.moveUp(settings["PADDLE_VELOCITY"])
    if keys[pygame.K_s]:
        paddleplayer1.moveDown(settings["PADDLE_VELOCITY"])
    if (not keys[pygame.K_w]) and (not keys[pygame.K_s]):
        paddleplayer1.action = 0

    if paddleplayer2.rect.midleft[1] < ball.rect.midleft[1]:
        paddleplayer2.moveDown(settings["PADDLE_VELOCITY"])
    elif paddleplayer2.rect.midleft[1] > ball.rect.midleft[1]:
        paddleplayer2.moveUp(settings["PADDLE_VELOCITY"] / 2)
    else:
        paddleplayer2.action = 0

    # points and reset
    if ball.rect.x > WINDOWWIDTH:
        paddleplayer1.scorePoint()
        ball.reset(1)

    if ball.rect.x < 0:
        paddleplayer2.scorePoint()
        ball.reset(0)

    # game end
    if (
        int(timer_s) - counter <= 0
        or paddleplayer1.getPoints() >= int(state["data"]["max_score"])
        or paddleplayer2.getPoints() >= int(state["data"]["max_score"])
    ):
        p1_name = state["data"]["p1_name"]
        p2_name = "CPU"
        winner = ""
        if paddleplayer1.getPoints() > paddleplayer2.getPoints():
            winner = p1_name
        elif paddleplayer1.getPoints() < paddleplayer2.getPoints():
            winner = p2_name
        else:
            winner = "draw"

        state["data"]["winner"] = winner
        state["n"] = 6  # go to end screen

    # elements display
    screen.fill(BLACK)
    paddleplayer1.draw(screen)
    paddleplayer2.draw(screen)
    ball.draw(screen)
    ball.bounce(paddleplayer1, paddleplayer2)
    draw_score(
        screen,
        (state["data"]["p1_name"], paddleplayer1.getPoints()),
        ("CPU", paddleplayer2.getPoints()),
    )
    screen.blit(font.render(timer, True, (WHITE)), (465, 10))
