import pygame


# defini la classe qui va gere le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):
    # constructor
    def __init__(self, player):
        super().__init__()
        print("[Create] : Projectile")
        self.velocity = player.velocity-1
        self.player = player
        self.image = pygame.image.load("PygameAssets-main/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # redimensionner
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def remove(self):
        self.player.all_projectiles.remove(self)

    def rotate(self):
        # tourner le projectile
        self.angle += 1
        self.image = pygame.transform.rotate(self.origin_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # si le projectile sort l'écran
        if self.rect.x > 1290:
            self.remove()
            print("[Delete] : Projectile")
