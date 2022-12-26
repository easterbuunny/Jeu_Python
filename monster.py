import random

import pygame

import animation


# creer une classe qui va gere la notion de monstre sur notre jeu
class Monster(animation.AnimateSprite):

    # constructor
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.startAnimation()
        self.lootAmount = 10

    def speedSet(self, speed):
        self.speedDefault = speed
        self.velocity = random.randint(1, self.speedDefault)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.speedDefault)
            self.health = self.maxHealth
            self.game.addScore(self.lootAmount)
            if self.game.cometEvent.isFull:
                self.game.allMonsters.remove(self)
                self.game.cometEvent.attemptFall()

    def updateAnimation(self):
        self.animate(loop=True)

    def updateHealthBar(self, surface):
        # definir une couleur pour une jauge de vie
        barColor = (111, 210, 46)  # creer une couleur
        backBarColor = (100, 100, 100)

        # definir la position de la jauge de vie
        barPosition = [self.rect.x + 20, self.rect.y - 20, self.health, 5]
        backBarPosition = [self.rect.x + 20, self.rect.y - 20, self.maxHealth, 5]

        # dessiner la barre de vie dans le jeu
        pygame.draw.rect(surface, backBarColor, backBarPosition)
        pygame.draw.rect(surface, barColor, barPosition)

    def forward(self):
        # deplacement s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.checkCollision(self, self.game.allPlayers):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)


class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.speedSet(3)


class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 120)
        self.health = 300
        self.maxHealth = 300
        self.speedSet(1)
        self.attack = 0.8
        self.lootAmount = 40
