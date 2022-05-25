import pygame
from item import Item
from ecrire_log import ecrire_log

class Vache:

    def __init__(self):
        self.image = pygame.image.load('image/vache.jpg')
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
        ecrire_log.ecrire_log(self=ecrire_log, texte=" info : vache produit")
        if self.produire_ou == "joueur":
            if joueur.verifie_puis_enleve("1 litre d'eau........10"):
                if joueur.verifie_puis_enleve("blé.....20"):
                    joueur.ajoute_inventer("1 litre de lait......40", 40)
        elif self.produire_ou == "boite":
            if boite.verifi_apartenance("1 litre d'eau........10"):
                if boite.verifi_apartenance("blé.....20"):
                    boite.items.append(Item(0, "1 litre de lait......40", 30, 40))
                    boite.enlever("1 litre d'eau........10")
                    boite.enlever("blé.....20")
        elif self.produire_ou == "vendre":
            if boite.verifi_apartenance("1 litre d'eau........10"):
                if boite.verifi_apartenance("blé.....20"):
                    boite.enlever("1 litre d'eau........10")
                    boite.enlever("blé.....20")
                    joueur.argent += 20
