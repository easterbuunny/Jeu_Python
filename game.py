import pygame

from cometEvent import CometFallEvent
from monster import Monster
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

    # creer une classe qui represente le jeu
    def checkCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def start(self):
        self.isPlaying = True
        self.spawnMonster()
        self.spawnMonster()

    def spawnMonster(self):
        monster = Monster(self)
        self.allMonsters.add(monster)

    def gameOver(self):
        self.allMonsters = pygame.sprite.Group()  # remove all monster
        self.player.health = self.player.maxHealth
        self.isPlaying = False

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        self.player.updateHealthBar(screen)

        self.cometEvent.updateBar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.allProjectiles:
            projectile.move()

        # recuperer les monstre du jeu
        for monster in self.allMonsters:
            monster.forward()
            monster.updateHealthBar(screen)

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
