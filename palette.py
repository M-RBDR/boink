#!/usr/bin/env python3

import pygame

class Palette():
    """Une classe pour gérer les palettes des joeurs."""


    def __init__(self, jeu, position):
        """Initialiser la palette et l'associer au jeu."""
        # Associer les attributs du jeu à la palette
        self.ecran = jeu.ecran
        self.ecran_rect = jeu.ecran.get_rect()
        self.parametres = jeu.parametres
        self.couleur = self.parametres.couleur_palette

        # Variables de gestion du mouvement afin d'assurer un mouvement continu
        self.mouvement_haut = False
        self.mouvement_bas = False

        # Créer un rect pour une palette et le mettre à la bonne position
        self.rect = pygame.Rect(0, 0, self.parametres.palette_largeur,
                                self.parametres.palette_hauteur)

        # Initialiser la position initiale de la palette à gauche ou à droite
        # de l'écran selon le paramètre position
        if position == 'gauche':
            self.rect.midleft = self.ecran_rect.midleft
            self.rect.x += self.parametres.palette_largeur
        elif position == 'droite':
            self.rect.midright = self.ecran_rect.midright
            self.rect.x -= self.parametres.palette_largeur


    def mise_a_jour(self):
        """Mettre à jour la position de la pallete
        selon la direction du mouvement."""
        # S'assurer que la palette reste dans l'espace de jeu
        if self.mouvement_haut and (self.rect.top > self.ecran_rect.top):
            self.rect.y -= 1
        if self.mouvement_bas and (self.rect.bottom < self.ecran_rect.bottom):
            self.rect.y += 1


    def afficher_palette(self):
        """Afficher la palette à l'écran."""
        pygame.draw.rect(self.ecran, self.couleur, self.rect)
