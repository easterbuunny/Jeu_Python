import random
import animation
import pygame


# creer une classe qui va gere la notion de monstre sur notre jeu
class Monster(animation.AnimateSprite):

    # constructor
    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.attack = 0.3
        self.image = pygame.image.load("PygameAssets-main/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.maxHealth
            if self.game.cometEvent.isFull:
                self.game.allMonsters.remove(self)
                self.game.cometEvent.attemptFall()

    def updateAnimation(self):
        self.animate()

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
