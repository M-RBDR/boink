#!/usr/bin/env python3

import sys

import pygame

from parametres import Parametres
from palette import Palette

class Jeu:
    """Une classe pour initialiser les attributs du jeu et gérer le jeu"""


    def __init__(self):
        """Initialiser le module pygame et les attributs du jeu"""
        pygame.init()

        self.parametres = Parametres()

        self.ecran = pygame.display.set_mode((self.parametres.ecran_largeur,
                                              self.parametres.ecran_hauteur))
        pygame.display.set_caption("Boink!")

        self.palettes = [Palette(self, 'gauche'), Palette(self, 'droite')]


    def _gerer_evenements(self):
        """Gérer les évènements du module pygame"""
        for event in pygame.event.get():
            # Vérifier si l'utilisateur veut quitter
            if event.type == pygame.QUIT:
                sys.exit()
            # Vérifier si une touche a été appuyée pour avoir
            # du mouvement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.palettes[0].mouvement_haut = True
                elif event.key == pygame.K_s:
                    self.palettes[0].mouvement_bas = True
                elif event.key == pygame.K_UP:
                    self.palettes[1].mouvement_haut = True
                elif event.key == pygame.K_DOWN:
                    self.palettes[1].mouvement_bas = True
            # Vérifier si une touche a été relâchée pour avoir
            # du mouvement continu
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.palettes[0].mouvement_haut = False
                elif event.key == pygame.K_s:
                    self.palettes[0].mouvement_bas = False
                elif event.key == pygame.K_UP:
                    self.palettes[1].mouvement_haut = False
                elif event.key == pygame.K_DOWN:
                    self.palettes[1].mouvement_bas = False


    def _mise_a_jour_acteurs(self):
        """Mettre à jour les acteurs du jeu."""
        for palette in self.palettes:
                palette.mise_a_jour()


    def _mise_a_jour_ecran(self):
        """Mettre à jour l'affichage et le présenter à l'utilisateur."""
        self.ecran.fill(self.parametres.couleur_fond)

        # Afficher les acteurs
        for palette in self.palettes:
            palette.afficher_palette()

        pygame.display.flip()


    def lancer_jeu(self):
        """Lancer la boucle du jeu."""
        while True:
            self._gerer_evenements()
            self._mise_a_jour_acteurs()
            self._mise_a_jour_ecran()


if __name__ == '__main__':
    jeu = Jeu()
    jeu.lancer_jeu()
