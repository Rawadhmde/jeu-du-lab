import pygame
import sys


pygame.init()

largeur, hauteur = 800, 600

fenetre = pygame.display.set_mode((largeur, hauteur))

pygame.display.set_caption("Jeu de Labyrinthe")

noir = (255,255,255)
blanc = (0,0,0)

class Joueur(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.image = pygame.Surface((30, 30))  # image de joueur aprés
        self.image.fill(blanc)
        self.rect = self.image.get_rect()
        self.rect.center = (largeur // 2, hauteur // 2)
        self.vitesse = 5

class Labyrinthe:

    def __init__(self):

        self.grille = [
            "XXXXXXXXXXXXXXWWXXXX",
            "X     X           X",
            "X XXXXX XXXXXXX XXX",
            "X X   X       XXXXX",
            "X X XXX XXXXX XXXxX",
            "X X X       X X   X",
            "X X XXXXXXX X XXXxX",
            "X X         X     X",
            "X XXXXXXXXX XXXXXxX",
            "X                 X",
            "XXXXXXXXXXXXXX  XXX",
        ]

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
labyrinthe = Labyrinthe()
joueur = Joueur()
for ligne, row in enumerate(labyrinthe.grille):
    for col, case in enumerate(row):
        if case == "X":
            pygame.draw.rect(fenetre, noir, (col * 40, ligne * 40, 40, 40))
        # Ajoutez ici le code pour les espaces vides

touches = pygame.key.get_pressed()
if touches[pygame.K_LEFT]:
    joueur.rect.x -= joueur.vitesse
if touches[pygame.K_RIGHT]:
    joueur.rect.x += joueur.vitesse
if touches[pygame.K_UP]:
    joueur.rect.y -= joueur.vitesse
if touches[pygame.K_DOWN]:
    joueur.rect.y += joueur.vitesse
