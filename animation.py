import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, spriteName, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'PygameAssets-main/{spriteName}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(spriteName)
        self.animation = False

    def startAnimation(self):
        self.animation = True

    def animate(self, loop=False):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# definir une fonction pour charger les image d'un sprite
def loadAnimationImage(spriteName):
    images = []  # tableau charge d'image
    path = f"PygameAssets-main/{spriteName}/{spriteName}"  # chemin de fichier
    for num in range(1, 24):
        imagePath = path + str(num) + '.png'
        images.append(pygame.image.load(imagePath))
    return images


animations = {
    'mummy': loadAnimationImage('mummy'),
    'player': loadAnimationImage('player'),
    'alien': loadAnimationImage('alien')
}
