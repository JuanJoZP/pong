import pygame
from config import BLACK, WHITE


def get_font(size):
    return pygame.font.SysFont("inkfree", size)


def end(screen, state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        pygame.quit()

    if state["data"]["winner"] != "draw":
        text2_string = state["data"]["winner"] + " wins!!!"
    else:
        text2_string = "It is a draw!!!"

    text1 = get_font(100).render("GAME OVER!", True, WHITE)
    text2 = get_font(80).render(text2_string, True, WHITE)

    # elements display
    screen.fill(BLACK)
    screen.blit(text1, text1.get_rect(center=(500, 200)))
    screen.blit(text2, text2.get_rect(center=(500, 300)))
