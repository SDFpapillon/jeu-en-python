import pygame
from math import *
from item import Item


class Boite_de_stocage():
    def __init__(self):
        self.police =pygame.font.SysFont(pygame.font.get_fonts()[8], 40)
        self.image_croix = pygame.image.load('image/croix.jpg')
        self.image_croix = pygame.transform.scale(self.image_croix, (50, 50))
        self.rect_croix = self.image_croix.get_rect()
        self.rect_croix.x = 765
        self.rect_croix.y = 20
        self.image = pygame.image.load('image/marche.jpg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = 10
        self.rect.x = 10
        # fléche page +/-
        self.image_fleche_gauche = pygame.image.load('image/gauche.jpg')
        self.image_fleche_gauche = pygame.transform.scale(self.image_fleche_gauche, (50, 50))
        self.rect_fleche_gauche = self.image_fleche_gauche.get_rect()
        self.rect_fleche_gauche.x = 625
        self.rect_fleche_gauche.y = 20
        self.image_fleche_droite = pygame.image.load('image/droite.jpg')
        self.image_fleche_droite = pygame.transform.scale(self.image_fleche_droite, (50, 50))
        self.rect_fleche_droite = self.image_fleche_droite.get_rect()
        self.rect_fleche_droite.x = 685
        self.rect_fleche_droite.y = 20
        # texte boite de stocage
        self.police_texte = pygame.font.SysFont(pygame.font.get_fonts()[8], 50)
        self.texte = self.police_texte.render("boite de stocage", True, (0, 0, 0))
        self.rect_texte = self.texte.get_rect()
        self.rect_texte.x = 250
        self.rect_texte.y = 30
        #liste des item des la boite
        self.items = []
        self.nombre_pages = 1
        self.nombre_pages_max = 1
        # pour la petite fenetre en plus a droite tu vois de quoi je parle?
        self.texte_vendre = self.police.render("- Vendre", True, (225, 0, 0))
        self.rect_vendre = self.texte_vendre.get_rect()
        self.rect_vendre.y = 50
        self.rect_vendre.x = 10
        self.texte_inventaire = self.police.render("- Inventaire", True, (0, 0, 0))
        self.rect_inventaire = self.texte_inventaire.get_rect()
        self.rect_inventaire.y = 100
        self.rect_inventaire.x = 10

    def MAJ_nombre_pages(self):
        longueur = len(self.items)
        if longueur == 0:
            longueur += 1
        longueur = ceil(longueur/10)
        self.nombre_pages_max = longueur

    def page_up(self):
        if self.nombre_pages == self.nombre_pages_max:
            self.nombre_pages = 1
        else:
            self.nombre_pages += 1

    def page_down(self):
        if self.nombre_pages == 1:
            self.nombre_pages = self.nombre_pages_max
        else:
            self.nombre_pages -= 1

    def deplace_inventaire(self, joueur, objet):
        if joueur.ajoute_inventer(objet.texte, objet.prix):
            self.items.remove(objet)

    def verifie_puis_enlever(self, item):
        if self.verifi_apartenance(item.texte):
            self.enlever(item.texte)
            return True

    def MAJ_des_items(self):
        for item in self.items:
            item.rect.y = -100
        y = 40
        for item in range((self.nombre_pages*10)-9 , self.nombre_pages*10):
            if item < len(self.items):
                y += 50
                self.items[item].rect.y = y

    def verifi_apartenance(self, item_to_check):
        for item in self.items:
            if item.texte == item_to_check:
                return True

    def ajouter(self, item, prix):
        if item != "rien":
            if "." in item:
                self.items.append(Item(0, item, 30, prix))

    def enlever(self, texte):
        for item in self.items:
            if item.texte == texte:
                self.items.remove(item)
                break
