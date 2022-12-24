from player import Player


# creer une classe qui represente le jeu
class Game():
    def __init__(self):
        print("[Create] : Game")
        self.player = Player() # Joueur
        self.pressed = {}  # les touches appuyés
