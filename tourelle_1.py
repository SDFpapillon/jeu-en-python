import pygame

class Tourelle_1:

    def __init__(self):
        self.image = pygame.image.load('image/tour_de_get.jpg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = -10
        self.rect.y = -10
        self.vitesse = 5
        self.degat = 10

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


    def attaquer_les_monstres(self, jeu):
        distance = 1000000
        for monstre in jeu.tout_monstre:
            if monstre.distance_joueur < distance:
                distance = monstre.distance_joueur
        for monstre in jeu.tout_monstre:
            if monstre.distance_joueur == distance:
                monstre.vie -= self.degat
