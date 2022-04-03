from config import WHITE, WINDOWHEIGHT, WIDTHp, HEIGHTp
import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  #pygame module with basic game object classes

        self.image = pygame. Surface((WIDTHp, HEIGHTp))  #Create an image of the paddle
        self.image.fill(WHITE)                # and add color

        self.rect = self.image.get_rect()     #Fetch the rectangle object

      
    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.top<=0:
            self.rect.top=0
    
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.bottom>=WINDOWHEIGHT:
            self.rect.bottom=WINDOWHEIGHT

    def draw(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))