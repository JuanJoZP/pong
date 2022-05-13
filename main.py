from ast import Import
import sys
import pygame
from paddle import Paddle
from ball import Ball
from button import Button
import config
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
    BALL_VELOCITY,
)
from score import draw_score

# window init
pygame.init()

icon = pygame.image.load("icon.xcf")
pygame.display.set_icon(icon)
pygame.display.set_caption("PONG")

screen = pygame.display.set_mode(SIZE)
screen.fill(BLACK)

clock = pygame.time.Clock()

# paddle and ball init
paddleplayer1 = Paddle()
paddleplayer1.rect.x = PADDLE_XSPACING
paddleplayer1.rect.y = WINDOWHEIGHT / 2 - PADDLE_HEIGHT / 2

paddleplayer2 = Paddle()
paddleplayer2.rect.x = WINDOWWIDTH - PADDLE_WIDTH - PADDLE_XSPACING
paddleplayer2.rect.y = WINDOWHEIGHT / 2 - PADDLE_HEIGHT / 2

ball = Ball()

#menu
#menu
def get_font(size):
    return pygame.font.SysFont("inkfree", size)

background = pygame.image.load("background.png")
background2 = pygame.image.load("Black.jpg")

def game_1():
    pass

def game_2():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        paddleplayer1.points == 0
        paddleplayer2.points == 0
        # key events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleplayer1.moveUp(config.PADDLE_VELOCITY)
        if keys[pygame.K_s]:
            paddleplayer1.moveDown(config.PADDLE_VELOCITY)
        if keys[pygame.K_UP]:
            paddleplayer2.moveUp(config.PADDLE_VELOCITY)
        if keys[pygame.K_DOWN]:
            paddleplayer2.moveDown(config.PADDLE_VELOCITY)
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
            break

        # elements display
        screen.fill(BLACK)
        paddleplayer1.draw(screen)
        paddleplayer2.draw(screen)
        ball.draw(screen)
        ball.bounce(paddleplayer1, paddleplayer2)
        draw_score(screen, paddleplayer1.getPoints(), paddleplayer2.getPoints())

        pygame.display.update()
        clock.tick(FPS)

def sett_ings():
    pygame.display.set_caption("Settings")
    while True:
        screen.blit(background2, (0,0))

        menu_mouse_position = pygame.mouse.get_pos()
        menu_text = get_font(50).render("Settings", True, "WHITE")
        paddle_text = get_font(50).render(f"{config.PADDLE_VELOCITY}", True, "WHITE")
        paddle_rect = paddle_text.get_rect(center = (465,270))
        ball_text = get_font(50).render(f"{config.BALL_VELOCITY}", True, "WHITE")
        ball_rect = ball_text.get_rect(center = (465,370))
        menu_rect = menu_text.get_rect(center = (465, 70))

        back_button = Button(position = (30, 30), input_text = "<", font = get_font(50), base_color = "WHITE", hovering_color = "#aaadaa")
        more_velocity_paddle = Button(position = (240, 270), input_text = "more paddle velocity", font = get_font(30), base_color = "WHITE", hovering_color = "#aaadaa")
        less_velocity_paddle = Button(position = (720, 270), input_text = "less paddle velocity", font = get_font(30), base_color = "WHITE", hovering_color = "#aaadaa")
        more_velocity_ball = Button(position = (240, 370), input_text = "more ball velocity", font = get_font(30), base_color = "WHITE", hovering_color = "#aaadaa")
        less_velocity_ball = Button(position = (720, 370), input_text = "less ball velocity", font = get_font(30), base_color = "WHITE", hovering_color = "#aaadaa")

        screen.blit(menu_text, menu_rect)
        screen.blit(paddle_text, paddle_rect)
        screen.blit(ball_text, ball_rect)
        
        for button in [more_velocity_paddle, less_velocity_paddle, more_velocity_ball, less_velocity_ball, back_button]:
            button.changeColor(menu_mouse_position)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(menu_mouse_position):
                    menu()
                if more_velocity_paddle.checkForInput(menu_mouse_position):
                    if config.PADDLE_VELOCITY==10:
                        pass
                    else:
                        config.PADDLE_VELOCITY +=1
                if less_velocity_paddle.checkForInput(menu_mouse_position):
                    if config.PADDLE_VELOCITY==5:
                        pass
                    else:
                        config.PADDLE_VELOCITY -=1
                if more_velocity_ball.checkForInput(menu_mouse_position):
                    if config.BALL_VELOCITY==15:
                        pass
                    else: 
                        config.BALL_VELOCITY +=1
                if less_velocity_ball.checkForInput(menu_mouse_position):
                    if config.BALL_VELOCITY==7:
                        pass
                    else: 
                        config.BALL_VELOCITY -=1
        paddle_text = get_font(50).render(f"{config.PADDLE_VELOCITY}", True, "WHITE")
        pygame.display.update()


def menu():
    pygame.display.set_caption("Menu")
    while True:
        screen.blit(background, (0,0))

        menu_mouse_position = pygame.mouse.get_pos()
        menu_text = get_font(100).render("Menu", True, "WHITE")
        menu_rect = menu_text.get_rect(center = (465, 70))

        play_with_cpu = Button(position = (465, 170), input_text = "1 Player", font = get_font(50), base_color = "WHITE", hovering_color = "#aaadaa")
        play_1vs1 = Button(position = (465, 270), input_text = "2 Players", font = get_font(50), base_color = "WHITE", hovering_color = "#aaadaa")
        settings = Button(position = (465, 370), input_text = "Settings", font = get_font(50), base_color = "WHITE", hovering_color = "#aaadaa")
        quit_game = Button(position = (465, 470), input_text = "Quit", font = get_font(50), base_color = "WHITE", hovering_color = "#aaadaa")

        screen.blit(menu_text, menu_rect)

        for button in [play_with_cpu, play_1vs1, settings, quit_game]:
            button.changeColor(menu_mouse_position)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_with_cpu.checkForInput(menu_mouse_position):
                    game_1()
                if play_1vs1.checkForInput(menu_mouse_position):
                    game_2()
                if settings.checkForInput(menu_mouse_position):
                    sett_ings()
                if quit_game.checkForInput(menu_mouse_position):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

menu()


#game()
#pygame.quit()
