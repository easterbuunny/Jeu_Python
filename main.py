import math

import pygame

from game import Game

print("\n\n===========================")
pygame.init()

# genere la fenetre de notre jeu
pygame.display.set_caption("Py Game")
print("[Title] : Py Game")
screen = pygame.display.set_mode((1080, 720))
print("[Windows Size] : 1290 * 720")
background = pygame.image.load('PygameAssets-main/bg.jpg')
print("[Load background] : OK")

# importer la banniere
banner = pygame.image.load('PygameAssets-main/banner.png')
print("[Load banner] : OK")
banner = pygame.transform.scale(banner, (500, 500))  # redimensionner l'image
bannerRect = banner.get_rect()
bannerRect.x = math.ceil(screen.get_width() / 4)

# importer le boutton
playButton = pygame.image.load('PygameAssets-main/button.png')
print("[Load button] : OK")
playButton = pygame.transform.scale(playButton, (400, 150))  # redimensionner l'image
buttonRect = playButton.get_rect()
buttonRect.x = math.ceil(screen.get_width() / 3.33)
buttonRect.y = math.ceil((screen.get_height() / 3) * 2)

game = Game()

running = True
# boucle tant que la condition Running est vrai (pour éviter que la fenetre s'eteint directement)
while running:
    # mettre le background dans screen
    screen.blit(background, (0, -200))  # width height

    # Verifier si le jeu a commencer ou non
    if game.isPlaying:
        game.update(screen)
    else:
        screen.blit(banner, bannerRect)
        screen.blit(playButton, buttonRect)

    # mettre a jour la fenetre
    pygame.display.flip()
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # l'evenement de fermeture
        if event.type == pygame.QUIT:
            running = False
            print("[Close the windows] : OK")
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # detecter la touche espace pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launchProjectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttonRect.collidepoint(event.pos):
                game.start()
