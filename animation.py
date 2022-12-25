import pygame

class AnimateSprite(pygame.sprite.Sprite) :

    def __init__(self, spriteName):
        super().__init__()
        self.image = pygame.image.load(f'PygameAssets-main/{spriteName}.png')

