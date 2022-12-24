import pygame

from game import Game

print("\n\n===========================")
pygame.init()

# genere la fenetre de notre jeu
pygame.display.set_caption("Py Game")
print("[Title] : Py Game")
screen = pygame.display.set_mode((1290, 720))
print("[Windows Size] : 1290 * 720")
background = pygame.image.load('PygameAssets-main/bg.jpg')
print("[Load background] : " + str(background))

game = Game()

running = True
# boucle tant que la condition Running est vrai (pour éviter que la fenetre s'eteint directement)
while running:
    # mettre le background dans screen
    screen.blit(background, (0, -200))  # width height
    screen.blit(game.player.image, game.player.rect)

    #recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #applique l'ensemble  des images  de mon groupe de projectile
    game.player.all_projectiles.draw(screen)

    # deplacement du joueur à l'écran
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.moveRigth()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.moveLeft()

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
