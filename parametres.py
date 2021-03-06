#!/usr/bin/env python3

class Parametres:
    """Une classe pour gérer les divers paramètres du jeu"""


    def __init__(self):
        """Initialiser les paramètres du jeu"""
        # Paramètres d'écran
        self.ecran_largeur = 800
        self.ecran_hauteur = 600
        self.couleur_fond = (30, 30, 80)

        # Paramètres des palettes
        self.palette_largeur = 20
        self.palette_hauteur = 80
        self.couleur_palette = (200, 200, 100)
        self.vitesse_palette = 300

        # Paramètres de la balle
        self.balle_largeur = 10
        self.balle_hauteur = 10
        self.couleur_balle = (200, 200, 100)
        self.vitesse_balle = 200
