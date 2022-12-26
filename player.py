import pygame
import animation

from projectile import Projectile


# creer une classe qui represente le joueur
class Player(animation.AnimateSprite):  # Pour créer un nouveau composant
    # Constructor
    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100  # PV
        self.maxHealth = 100  # PV max
        self.attack = 20  # degat attaque
        self.velocity = 2  # vitesse de mouvement en pixel
        self.rect = self.image.get_rect()
        self.rect.x = 400  # position axe x
        self.rect.y = 500  # position axe y
        self.allProjectiles = pygame.sprite.Group()

    def launchProjectile(self):
        projectile = Projectile(self)
        self.allProjectiles.add(projectile)
        self.startAnimation()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.gameOver()

    def moveRight(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.checkCollision(self, self.game.allMonsters):
            self.rect.x += self.velocity

    def moveLeft(self):
        self.rect.x -= self.velocity

    def updateAnimate(self):
        self.animate()

    def updateHealthBar(self, surface):
        # definir une couleur pour une jauge de vie
        barColor = (111, 210, 46)  # creer une couleur
        backBarColor = (100, 100, 100)

        # definir la position de la jauge de vie
        barPosition = [self.rect.x + 50, self.rect.y + 30, self.health, 7]
        backBarPosition = [self.rect.x + 50, self.rect.y + 30, self.maxHealth, 7]

        # dessiner la barre de vie dans le jeu
        pygame.draw.rect(surface, backBarColor, backBarPosition)
        pygame.draw.rect(surface, barColor, barPosition)
