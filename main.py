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

        self.palettes = []
        self.palettes.append(Palette(self, 'gauche'))
        self.palettes.append(Palette(self, 'droite'))

        self.palettes_affichage = pygame.sprite.Group()
        self.palettes_affichage.add(self.palettes[0])
        self.palettes_affichage.add(self.palettes[1])


    def _gerer_evenements(self):
        """Gérer les évènements du module pygame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.palettes[0].mouvement_haut = True
                elif event.key == pygame.K_DOWN:
                    self.palettes[0].mouvement_bas = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.palettes[0].mouvement_haut = False
                elif event.key == pygame.K_DOWN:
                    self.palettes[0].mouvement_bas = False


    def _mise_a_jour_ecran(self):
        """Mettre à jour l'affichage et le présenter à l'utilisateur"""
        self.ecran.fill(self.parametres.couleur_fond)

        for palette in self.palettes:
            palette.afficher_palette()

        pygame.display.flip()


    def lancer_jeu(self):
        """lancer la boucle du jeu"""
        while True:
            self._gerer_evenements()
            for palette in self.palettes_affichage.sprites():
                palette.mise_a_jour()
            self._mise_a_jour_ecran()

if __name__ == '__main__':
    jeu = Jeu()
    jeu.lancer_jeu()
