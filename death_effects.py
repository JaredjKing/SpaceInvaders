import pygame
from pygame.sprite import Sprite




class Explosion(Sprite):

    def __init__(self):
        super().__init__()
        self.image_raw = pygame.image.load('images/boom.bmp')
        self.image = pygame.transform.scale(self.image_raw, (50, 50))



