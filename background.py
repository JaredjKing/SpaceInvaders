import pygame
from settings import Settings


class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        self.settings = Settings()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/space-bkgrd.bmp')
        self.background = pygame.transform.scale(self.image,
                                                 (self.settings.screen_width, self.settings.screen_height))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
