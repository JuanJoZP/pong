from config import WHITE, WINDOWHEIGHT, WINDOWWIDTH
import pygame
import random
velocity = 3

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  #pygame module with basic game object classes

        self.image = pygame. Surface((10, 10))  #Create an image of the paddle
        self.image.fill(WHITE)                # and add color

        self.rect = self.image.get_rect()     #Fetch the rectangle object
        self.rect.x = WINDOWWIDTH / 2
        self.rect.y = WINDOWHEIGHT / 2
        self.direction = (velocity, 0)

      
    def move(self):
        self.rect.x+=self.direction[0]
        self.rect.y+=self.direction[1]

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
        
    def bounce(self,p1,p2):
        if self.rect.left== p1.rect.right:
            self.direction=(-velocity,random.randint(-3,3))
        if self.rect.right==p2.rect.left:
            self.direction=(-velocity,random.randint(-3,3))