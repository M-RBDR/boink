#!/usr/bin/env python3

import pygame

import random

class Balle:
    """Une classe pour gérer les attributs et les méthodes d'une balle."""


    def __init__(self, jeu):
        """Initialiser la balle et l'associer au jeu."""
        # Associer les attributs du jeu à la balle
        self.ecran = jeu.ecran
        self.ecran_rect = jeu.ecran.get_rect()
        self.palettes = jeu.palettes
        self.parametres = jeu.parametres
        self.couleur = self.parametres.couleur_balle

        # Créer un rect pour la balle et le mettre à la bonne position
        self.rect = pygame.Rect(0, 0, self.parametres.balle_largeur,
                                self.parametres.balle_hauteur)

        # Initialiser la position de la balle au centre de l'écran
        self.rect.center = self.ecran_rect.center

        # Créer des variables directions et leur donner une valeur aléatoire
        self.direction_x = int(random.choice([-1, 1]))
        self.direction_y = int(random.choice([-1, 1]))


    def mise_a_jour(self, delta_temps):
        """Mettre à jour la position de la balle
        selon la direction du mouvement."""
        # S'assurer que la balle reste dans l'espace de jeu à la verticale
        if self.rect.top <= self.ecran_rect.top:
            self.direction_y = -self.direction_y
        elif self.rect.bottom >= self.ecran_rect.bottom:
            self.direction_y = -self.direction_y

        # Faire bondire dans le sens opposé la balle
        # lorsqu'elle entre en contacte avec une palette
        for palette in self.palettes:
            if pygame.Rect.colliderect(palette.rect, self.rect):
                if palette.rect.center > self.ecran_rect.center:
                    self.rect.right = palette.rect.left
                elif palette.rect.center < self.ecran_rect.center:
                    self.rect.left = palette.rect.right
                self.direction_x = -self.direction_x

        # Mouvement de la balle
        self.rect.x += self.direction_x * self.parametres.vitesse_balle * delta_temps
        self.rect.y += self.direction_y * self.parametres.vitesse_balle * delta_temps


    def afficher(self):
        """Afficher la balle à l'écran."""
        pygame.draw.rect(self.ecran, self.couleur, self.rect)
