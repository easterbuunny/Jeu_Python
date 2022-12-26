import random

import pygame

from monster import Mummy


class Comet(pygame.sprite.Sprite):

    def __init__(self, cometEvent):
        super().__init__()
        self.image = pygame.image.load('PygameAssets-main/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 5)
        self.rect.x = random.randint(10, 1000)
        self.rect.y = - random.randint(0, 800)
        self.cometEvent = cometEvent
        self.attack = 20

    def remove(self):
        self.cometEvent.allComet.remove(self)
        if len(self.cometEvent.allComet) == 0:
            self.cometEvent.resetPercent()
            self.cometEvent.game.start()

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 500:
            self.remove()
            if len(self.cometEvent.allComet) == 0:
                self.cometEvent.resetPercent()
                self.cometEvent.fallMode = False
        if self.cometEvent.game.checkCollision(self, self.cometEvent.game.allPlayers):
            self.remove()
            self.cometEvent.game.player.damage(self.attack)
