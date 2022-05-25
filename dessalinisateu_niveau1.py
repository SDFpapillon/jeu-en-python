import pygame
from item import Item

class dessalinisateur_niveau1:

    def __init__(self):
        self.image = pygame.image.load('image/usine.jpg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.pose = False
        self.vitesse = 5
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
        if self.produire_ou == "vendre":
            joueur.argent += 5
        elif self.produire_ou == "boite":
            boite.items.append(Item(0, "1 litre d'eau........10", 30, 10))
