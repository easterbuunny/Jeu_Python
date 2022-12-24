import pygame
from projectile import Projectile


# creer une classe qui represente le joueur
class Player(pygame.sprite.Sprite):  # Pour créer un nouveau composant
    # Constructor
    def __init__(self):
        print("[Create] : Player")
        super().__init__()
        self.health = 100  # PV
        self.maxHealth = 100  # PV max
        self.attack = 10  # degat attaque
        self.velocity = 3  # vitesse de mouvement en pixel
        self.image = pygame.image.load("PygameAssets-main/player.png") #image du joueur
        self.rect = self.image.get_rect()
        self.rect.x = 400 # position axe x
        self.rect.y = 500 # position axe y
        self.all_projectiles = pygame.sprite.Group()

    def launchProjectile(self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def moveRigth(self):
        self.rect.x += self.velocity

    def moveLeft(self):
        self.rect.x -= self.velocity
