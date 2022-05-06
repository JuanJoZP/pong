from config import WHITE, WINDOWHEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT
import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.points = (
            0  # DEV: usar esta variable para mostrar los puntos en la interfaz
        )
        self.action = 0  # 1- for up 1 for down (used in Ball())

        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        self.action = -1
        if self.rect.top <= 0:
            self.rect.top = 0

    def moveDown(self, pixels):
        self.action = 1
        self.rect.y += pixels
        if self.rect.bottom >= WINDOWHEIGHT:
            self.rect.bottom = WINDOWHEIGHT

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def scorePoint(self):
        self.points += 1
