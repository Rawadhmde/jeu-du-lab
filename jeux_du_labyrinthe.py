import pygame
import sys
from class_du_jeu import *

pygame.init()

largeur, hauteur = 800, 600

fenetre = pygame.display.set_mode((largeur, hauteur))

pygame.display.set_caption("Jeu de Labyrinthe")
