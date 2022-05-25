import pygame
from item import Item
from ecrire_log import ecrire_log


#gréation de la class joueur
class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.je_peux_mourir = True
        self.recharge = 0
        self.vivant = True
        #pour l'inventer
        self.police = pygame.font.SysFont(pygame.font.get_fonts()[8], 40)
        self.image_croix_joueur = pygame.image.load('image/croix.jpg')
        self.image_croix_joueur = pygame.transform.scale(self.image_croix_joueur, (50, 50))
        self.rect_croix_joueur = self.image_croix_joueur.get_rect()
        self.rect_croix_joueur.x = 765
        self.rect_croix_joueur.y = 20
        #pour la petite fenetre en plus a droite tu vois de quoi je parle?
        self.texte_utilise = self.police.render("- Utiliser", True, (0, 0, 0))
        self.rect_utilise = self.texte_utilise.get_rect()
        self.rect_utilise.y = 50
        self.rect_utilise.x = 10
        self.texte_vendre = self.police.render("- Vendre", True, (225, 0, 0))
        self.rect_vendre = self.texte_vendre.get_rect()
        self.rect_vendre.y = 150
        self.rect_vendre.x = 10
        self.texte_boite = self.police.render("- Boite", True, (0, 0, 0))
        self.rect_boite = self.texte_boite.get_rect()
        self.rect_boite.y = 100
        self.rect_boite.x = 10
        #variable de vie
        self.eau = 100
        self.nouriture = 100
        self.degat = 0.1
        # texte boite de stocage
        self.police_texte = pygame.font.SysFont(pygame.font.get_fonts()[8], 50)
        self.texte = self.police_texte.render("inventaire", True, (0, 0, 0))
        self.rect_texte = self.texte.get_rect()
        self.rect_texte.x = 250
        self.rect_texte.y = 30
        #le reste
        self.vitesse = 5
        self.image = pygame.image.load('image/joueur.jpg')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.argent = 100
        #re l'inventer
        self.inventer = {
            1 : Item(90, "rien", 30, 0),
            2 : Item(140, "rien", 30, 0),
            3 : Item(190, "rien", 30, 0),
            4 : Item(240, "rien", 30, 0),
            5 : Item(290, "rien", 30, 0),
            6 : Item(340, "rien", 30, 0),
            7 : Item(390, "rien", 30, 0),
            8 : Item(440, "rien", 30, 0),
            9 : Item(490, "rien", 30, 0),
            10 : Item(540, "rien", 30, 0)
        }
        self.nouriture_liste = [
            "poisson.......10",
            "gros poisson.......20",
            "maïs......10",
            "poulet cuit........30",
            "pain.......30",
            "blé.....20",
            "1 litre de lait......40",
            "1 litre d'eau........10"
        ]
        self.batiment_liste = [
            "dessalinisateur niveau 1........70",
            "pousse de maïs......50",
            "pousse de blé......90",
            "vache.......180",
            "tourelle de combat....450",
            "centrale au charbon.....6000",
            "mine.......10000",
            "mine niveau 2",
            "atelier a batiment....1000",
        ]

    def add_nouriture(self, item):
        ecrire_log.ecrire_log(self=ecrire_log, texte=" info : ajout nouriture")
        if item.texte == self.nouriture_liste[0]:
            self.nouriture += 10
        elif item.texte == self.nouriture_liste[1]:
            self.nouriture += 20
        elif item.texte == self.nouriture_liste[2]:
            self.nouriture += 10
        elif item.texte == self.nouriture_liste[3]:
            self.nouriture += 40
        elif item.texte == self.nouriture_liste[4]:
            self.nouriture += 50
        elif item.texte == self.nouriture_liste[5]:
            self.nouriture += 10
        elif item.texte == self.nouriture_liste[6]:
            self.nouriture += 10
            self.eau += 5
        elif item.texte == self.nouriture_liste[7]:
            self.eau += 10

    def ajoute_inventer(self, objet, prix):
        ecrire_log.ecrire_log(self=ecrire_log, texte=" info : ajout a l'inventaire")
        for i in self.inventer:
            if self.inventer[i].texte == "rien":
                self.inventer[i] = Item(self.inventer[i].rect.y, objet, 30, prix)
                return True
        return False

    def verif_inventair(self, objet):
        ecrire_log.ecrire_log(self=ecrire_log, texte=" info : verifit l'apartenance a l'inventaire")
        for i in self.inventer:
            if self.inventer[i].texte == objet:
                return True

    def MouvementDroite(self):
        if self.rect.x <= 1030:
            self.rect.x += self.vitesse
            if self.nouriture > 0:
                self.nouriture -= 0.1
            else:
                self.mourir()

    def MouvementGauche(self):
        if self.rect.x >= 0:
            self.rect.x -= self.vitesse
            if self.nouriture > 0:
                self.nouriture -= 0.1
            else:
                self.mourir()

    def MouvementHaut(self):
        if self.rect.y >= 0:
            self.rect.y -= self.vitesse
            if self.nouriture > 0:
                self.nouriture -= 0.1
            else:
                self.mourir()

    def MouvementBas(self):
        if self.rect.y <=  650:
            self.rect.y += self.vitesse
            if self.nouriture > 0:
                self.nouriture -= 0.1
            else:
                self.mourir()

    def detaille_inventaire(self, ecran):
        pygame.draw.rect(ecran, (255, 255, 255), [240, 20, 595, 660])

    def enlever_item(self, item, y):
        self.inventer[item] = Item(y, "rien", 30, 0)

    def verifie_puis_enleve(self, objet):
        for i in self.inventer:
            if self.inventer[i].texte == objet:
                self.enlever_item(i, self.inventer[i].rect.y)
                return True

    def attaque(self, tout_monstre):
        ecrire_log.ecrire_log(self=ecrire_log, texte=" info : attaque du joueur")
        distance = 100000
        for monstre in tout_monstre:
            if monstre.distance_joueur < distance:
                distance = monstre.distance_joueur
        if self.verif_inventair("mousquet......500"):
            self.recharge += 1
            if self.recharge == 5:
                self.recharge = 0
                self.degat = 5

        elif self.verif_inventair("arc........140"):
            self.degat = 1

        else:
            self.degat = 0.1
        for monstre in tout_monstre:
            if monstre.distance_joueur == distance:
                monstre.vie -= self.degat
            if monstre.distance_joueur == 0:
                self.nouriture -= 1

    def mourir(self):
        if self.je_peux_mourir:
            ecrire_log.ecrire_log(self=ecrire_log, texte=" info : le joueur meurt")
            self.vivant = False
            sauvegarde = open('sauvegarde', 'w', 1)
            sauvegarde.write("false \n")
            sauvegarde.close()