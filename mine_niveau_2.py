import pygame
from item import Item
from ecrire_log import ecrire_log
import random

class Mine_niveau_2:

    def __init__(self):
        self.image = pygame.image.load('image/mine_niveau_2.jpg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.vitesse = 5
        self.degat = 10
        self.produire_ou = "boite"

    def MouvementDroite(self):
        if self.rect.x <= 1030:
            self.rect.x += self.vitesse

    def MouvementGauche(self):
        if self.rect.x >= 0:
            self.rect.x -= self.vitesse

    def MouvementHaut(self):
        if self.rect.y >= 0:
            self.rect.y -= self.vitesse

    def MouvementBas(self):
        if self.rect.y <=  650:
            self.rect.y += self.vitesse

    def produire(self, joueur, boite):
        chance = random.randint(1, 1000)
        ecrire_log.ecrire_log(ecrire_log, " info : mine produit")
        if chance <= 500:
            if self.produire_ou == "vendre":
                joueur.argent += 20
            elif self.produire_ou == "boite":
                boite.items.append(Item(0, "charbon......40", 30, 40))
            elif self.produire_ou == "joueur":
                joueur.ajoute_inventer("charbon......40", 40)
        elif chance <= 745:
            if self.produire_ou == "vendre":
                joueur.argent += 50
            elif self.produire_ou == "boite":
                boite.items.append(Item(0, "cuivre.....100", 30, 100))
        elif chance <= 895:
            if self.produire_ou == "vendre":
                joueur.argent += 75
            elif self.produire_ou == "boite":
                boite.items.append(Item(0, "fer.....150", 30, 150))
        elif chance <= 995:
            if self.produire_ou == "vendre":
                joueur.argent += 250
            elif self.produire_ou == "boite":
                boite.items.append(Item(0, "or.....500", 30, 500))
        else:
            if self.produire_ou == "vendre":
                joueur.argent += 500
            elif self.produire_ou == "boite":
                boite.items.append(Item(0, "diamant....1000", 30, 1000))
