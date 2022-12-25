import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, spriteName):
        super().__init__()
        self.image = pygame.image.load(f'PygameAssets-main/{spriteName}.png')
        self.current_image = 0
        self.images = animations.get(spriteName)

    def animate(self):
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.image = self.images[self.current_image]


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
    'player': loadAnimationImage('player')
}
