import pygame

from comet import Comet


class CometFallEvent:
    # constructor
    def __init__(self, game):
        self.percent = 0
        self.percentSpeed = 20
        self.allComet = pygame.sprite.Group()
        self.game = game
        self.fallMode = False

    def addPercent(self):
        self.percent += self.percentSpeed / 100

    def isFull(self):
        return self.percent >= 100

    def resetPercent(self):
        self.percent = 0

    def enableMeteor(self):
        for i in range(1, 10):
            comet = Comet(self)
            self.allComet.add(comet)

    def attemptFall(self):
        if self.isFull() and len(self.game.allMonsters) == 0:
            print("Pluie de cometes !")
            self.enableMeteor()
            self.fallMode = True

    def updateBar(self, surface):
        # Ajouter du pourcentage
        self.addPercent()

        # barre noir en arriere plan
        pygame.draw.rect(surface, (0, 0, 0),
                         [
                             0,  # x
                             surface.get_height() - 5,  # y
                             surface.get_width(),  # longueur de la fenetre
                             10  # epaisseur
                         ])
        # barre rouge, qui est l'evenement
        pygame.draw.rect(surface, (187, 11, 11),
                         [
                             0,  # x
                             surface.get_height() - 5,  # y
                             (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
                             10  # epaisseur
                         ])
