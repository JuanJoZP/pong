import pygame
from config import (
    PAUSE_TIME,
    WHITE,
    WINDOWHEIGHT,
    WINDOWWIDTH,
    FPS,
    settings,
    DIRECTION_MULTIPLIER,
    DIRECTION_MAX,
)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = WINDOWWIDTH / 2  # initial position
        self.rect.y = WINDOWHEIGHT / 2
        self.direction = (-settings["BALL_VELOCITY"], 0)  # start moving right

        self.pause = PAUSE_TIME  # pause in seconds, only for the ball

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
        self._move()

    def bounce(self, p1, p2):
        current_direction = self.direction
        ball_rect = self.rect

        # paddle collision
        if ball_rect.colliderect(p1.rect):
            self.direction = (
                -current_direction[0],
                self._apply_new_y(current_direction[1], p1.action),
            )
        if ball_rect.colliderect(p2.rect):
            self.direction = (
                -current_direction[0],
                self._apply_new_y(current_direction[1], p2.action),
            )

        # border collision
        if ball_rect.top <= 0 or ball_rect.bottom >= WINDOWHEIGHT:
            self.direction = (current_direction[0], -current_direction[1])

    def reset(self, direction):
        self.rect.x = WINDOWWIDTH / 2
        self.rect.y = WINDOWHEIGHT / 2

        if direction:  # 1 for right, 0 for left
            self.direction = (settings["BALL_VELOCITY"], 0)
        else:
            self.direction = (-settings["BALL_VELOCITY"], 0)

        self.pause = PAUSE_TIME

    def _move(self):
        if self.pause >= 0:
            self.pause -= 1 / FPS
            return

        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def _apply_new_y(self, ball_y, paddle_y):
        if abs(ball_y + paddle_y * DIRECTION_MULTIPLIER) > DIRECTION_MAX:
            return ball_y  # the direction does not change if it gets over the max

        return ball_y + paddle_y * DIRECTION_MULTIPLIER
