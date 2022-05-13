import pygame
from button import Button
import sys

background = pygame.image.load("background.png")


def get_font(size):
    return pygame.font.SysFont("inkfree", size)


def menu(screen, state):
    pygame.display.set_caption("Menu")

    screen.blit(background, (0, 0))

    menu_mouse_position = pygame.mouse.get_pos()
    menu_text = get_font(100).render("Menu", True, "WHITE")
    menu_rect = menu_text.get_rect(center=(465, 70))

    play_with_cpu = Button(
        position=(465, 170),
        input_text="1 Player",
        font=get_font(50),
        base_color="WHITE",
        hovering_color="#aaadaa",
    )
    play_1vs1 = Button(
        position=(465, 270),
        input_text="2 Players",
        font=get_font(50),
        base_color="WHITE",
        hovering_color="#aaadaa",
    )
    settings = Button(
        position=(465, 370),
        input_text="Settings",
        font=get_font(50),
        base_color="WHITE",
        hovering_color="#aaadaa",
    )
    quit_game = Button(
        position=(465, 470),
        input_text="Quit",
        font=get_font(50),
        base_color="WHITE",
        hovering_color="#aaadaa",
    )

    screen.blit(menu_text, menu_rect)

    for button in [play_with_cpu, play_1vs1, settings, quit_game]:
        button.changeColor(menu_mouse_position)
        button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_with_cpu.checkForInput(menu_mouse_position):
                pass  # state["n"] = 1
            if play_1vs1.checkForInput(menu_mouse_position):
                state["n"] = 2
            if settings.checkForInput(menu_mouse_position):
                state["n"] = 3
            if quit_game.checkForInput(menu_mouse_position):
                sys.exit()
