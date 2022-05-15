import pygame
import config
from button import Button
import sys
import menu

background2 = pygame.image.load("Black.jpg")


def get_font(size):
    return pygame.font.SysFont("inkfree", size)


def settings(screen, state):
    screen.blit(background2, (0, 0))

    paddle_v = config.settings["PADDLE_VELOCITY"]
    ball_v = config.settings["BALL_VELOCITY"]

    # get all the texts
    menu_mouse_position = pygame.mouse.get_pos()
    menu_text = get_font(50).render("Settings", True, "WHITE")
    paddle_text = get_font(50).render(f"{paddle_v}", True, "WHITE")
    paddle_rect = paddle_text.get_rect(center=(465, 270))
    ball_text = get_font(50).render(f"{ball_v}", True, "WHITE")
    ball_rect = ball_text.get_rect(center=(465, 370))
    menu_rect = menu_text.get_rect(center=(465, 70))

    # button init
    back_button = Button(
        position=(30, 30),
        input_text="<",
        font=get_font(50),
        base_color="WHITE",
        hovering_color="#aaadaa",
    )
    more_velocity_paddle = Button(
        position=(240, 270),
        input_text="more paddle velocity",
        font=get_font(30),
        base_color="WHITE",
        hovering_color="#aaadaa",
    )
    less_velocity_paddle = Button(
        position=(720, 270),
        input_text="less paddle velocity",
        font=get_font(30),
        base_color="WHITE",
        hovering_color="#aaadaa",
    )
    more_velocity_ball = Button(
        position=(240, 370),
        input_text="more ball velocity",
        font=get_font(30),
        base_color="WHITE",
        hovering_color="#aaadaa",
    )
    less_velocity_ball = Button(
        position=(720, 370),
        input_text="less ball velocity",
        font=get_font(30),
        base_color="WHITE",
        hovering_color="#aaadaa",
    )

    screen.blit(menu_text, menu_rect)
    screen.blit(paddle_text, paddle_rect)
    screen.blit(ball_text, ball_rect)

    for button in [
        more_velocity_paddle,
        less_velocity_paddle,
        more_velocity_ball,
        less_velocity_ball,
        back_button,
    ]:
        button.changeColor(menu_mouse_position)
        button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # button events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button.checkForInput(menu_mouse_position):
                state["n"] = 0
            if more_velocity_paddle.checkForInput(menu_mouse_position):
                if config.settings["PADDLE_VELOCITY"] == 10:
                    pass
                else:
                    config.settings["PADDLE_VELOCITY"] += 1
            if less_velocity_paddle.checkForInput(menu_mouse_position):
                if config.settings["PADDLE_VELOCITY"] == 5:
                    pass
                else:
                    config.settings["PADDLE_VELOCITY"] -= 1
            if more_velocity_ball.checkForInput(menu_mouse_position):
                if config.settings["BALL_VELOCITY"] == 15:
                    pass
                else:
                    config.settings["BALL_VELOCITY"] += 1
            if less_velocity_ball.checkForInput(menu_mouse_position):
                if config.settings["BALL_VELOCITY"] == 7:
                    pass
                else:
                    config.settings["BALL_VELOCITY"] -= 1
    paddle_text = get_font(50).render(f"{paddle_v}", True, "WHITE")
