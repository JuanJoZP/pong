from time import time
import pygame
from config import BLACK, WHITE


pygame.init()
font = pygame.font.SysFont("inkfree", 25)
input_rect = pygame.Rect(200, 230, 140, 32)
label_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color(178, 178, 178)
color_passive = pygame.Color(158, 158, 158)
color = color_passive
active = False

p1_name = ""
p2_name = ""
timer_s = ""
max_score = ""
inputs_responses = [
    timer_s,
    max_score,
    p1_name,
    p2_name,
]
inputs_label = [
    "Enter the seconds of duration of the game",
    "Enter the score at which the game ends",
    "Enter the name of player 1",
    "Enter the name of player 2",
]
curr_input = 0


def inputs(screen, state, new_state):
    global color, curr_input, active

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_passive
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN and inputs_responses[curr_input] != "":
                curr_input += 1
            elif event.key == pygame.K_BACKSPACE:
                inputs_responses[curr_input] = inputs_responses[curr_input][:-1]
            else:
                inputs_responses[curr_input] += event.unicode

    # elements display

    if curr_input == 4:
        state["n"] = new_state
        state["data"] = {
            "p1_name": inputs_responses[2],
            "p2_name": inputs_responses[3],
            "timer_s": inputs_responses[0],
            "max_score": inputs_responses[1],
        }
    elif curr_input == 3 and new_state == 4:
        state["n"] == new_state
        state["data"] = {
            "p1_name": inputs_responses[2],
            "timer_s": inputs_responses[0],
            "max_score": inputs_responses[1],
        }
    else:
        input_surface = font.render(inputs_responses[curr_input], True, (WHITE))
        label_surface = font.render(inputs_label[curr_input], True, (WHITE))

        screen.fill(BLACK)
        pygame.draw.rect(screen, color, input_rect)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
        screen.blit(label_surface, (label_rect.x, label_rect.y))
