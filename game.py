import random

import pygame

from cometEvent import CometFallEvent
from monster import Mummy, Alien
from player import Player


class Game:
    def __init__(self):
        self.isPlaying = False
        self.allPlayers = pygame.sprite.Group()
        self.player = Player(self)  # Joueur
        self.allPlayers.add(self.player)
        self.cometEvent = CometFallEvent(self)
        self.allMonsters = pygame.sprite.Group()  # groupe de monster
        self.pressed = {}  # les touches appuyés
        self.score = 0
        self.font = pygame.font.SysFont("monospace", 32)

    # creer une classe qui represente le jeu
    def checkCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def start(self):
        self.isPlaying = True
        for i in range(0, random.randint(2, 5)):
            self.spawnMonster(Mummy)
        if self.cometEvent.counter >=3 :
            self.spawnMonster(Alien)
        if self.cometEvent.counter >=6 :
            self.spawnMonster(Alien)
            self.spawnMonster(Alien)

    def addScore(self, points):
        self.score += points

    def spawnMonster(self, monsterName):
        self.allMonsters.add(monsterName.__call__(self))

    def gameOver(self):
        print("[Level] : " + str(self.cometEvent.counter))
        print("[Score] : " + str(self.score))
        self.allMonsters = pygame.sprite.Group()  # remove all monster
        self.player.health = self.player.maxHealth
        self.isPlaying = False
        self.allPlayers = pygame.sprite.Group()
        self.cometEvent.allComet = pygame.sprite.Group()
        self.cometEvent.counter = 1
        self.score = 0

    def update(self, screen):
        # text et police score

        scoreText = self.font.render(f"Score :{self.score}", True, (0, 0, 0))
        screen.blit(scoreText, (20, 20))

        level = self.font.render(f"Level :{self.cometEvent.counter}", True, (0, 0, 0))
        screen.blit(level, (800, 20))

        screen.blit(self.player.image, self.player.rect)

        self.player.updateHealthBar(screen)
        self.player.animate()

        self.cometEvent.updateBar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.allProjectiles:
            projectile.move()

        # recuperer les monstre du jeu
        for monster in self.allMonsters:
            monster.forward()
            monster.updateHealthBar(screen)
            monster.updateAnimation()

        for comet in self.cometEvent.allComet:
            comet.fall()

        # applique l'ensemble  des images  de mon groupe de projectile
        self.player.allProjectiles.draw(screen)

        # appliquer l'ensemble d'images de mon groupe de monstre
        self.allMonsters.draw(screen)

        self.cometEvent.allComet.draw(screen)

        # deplacement du joueur à l'écran
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.moveRight()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.moveLeft()
