import pygame
from item import Item
from ecrire_log import ecrire_log

class Atelier_batiment:

    def __init__(self):
        self.afichage_plus = "rien"
        self.police_article = pygame.font.SysFont(pygame.font.get_fonts()[8], 30)
        self.texte_achat = self.police_article.render("CREER", True, (0, 128, 0))
        self.texte_achat_rect = self.texte_achat.get_rect()
        self.texte_achat_rect.x = 550
        self.police = pygame.font.SysFont(pygame.font.get_fonts()[8], 40)
        self.nombre_fer = 0
        self.nombre_or = 0
        self.nombre_charbon = 0
        self.nombre_cuivre = 0
        self.nombre_diament = 0
        self.page_utilise = 1
        self.max_page = 1
        self.police = pygame.font.SysFont(pygame.font.get_fonts()[8], 40)
        self.image_croix = pygame.image.load('image/croix.jpg')
        self.image_croix = pygame.transform.scale(self.image_croix, (50, 50))
        self.rect_croix = self.image_croix.get_rect()
        self.rect_croix.x = 765
        self.rect_croix.y = 20
        self.prix_objet = 0
        self.type_objet = "rien"
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
        # texte marché
        self.police_texte = pygame.font.SysFont(pygame.font.get_fonts()[8], 50)
        self.texte = self.police_texte.render("atelier a batiment", True, (0, 0, 0))
        self.rect_texte = self.texte.get_rect()
        self.rect_texte.x = 250
        self.rect_texte.y = 30
        #item
        self.item_page_1 = [
            Item(90, "mine niveau 2", 30, 500)
        ]

        self.texte_i1_p1_P1 = self.police_article.render("La mine niveau 2 permet une meilleur production que la", True, (0, 0, 0))
        self.texte_i1_p1_P2 = self.police_article.render("mine niveau 1. Elle ne produit pas plus mais elle produit",True, (0, 0, 0))
        self.texte_i1_p1_P3 = self.police_article.render("plus de minerais rare. Elle demande 10 fer, 20 charbon et ", True, (0, 0, 0))
        self.texte_i1_p1_P4 = self.police_article.render("un or pour être construite.", True, (0, 0, 0))

    def afichage_etablie(self, ecran, boite, liste_batiment):
        self.ecran = ecran
        self.boite = boite
        self.liste_batiment  = liste_batiment
        pygame.draw.rect(ecran, (255, 255, 255), [240, 20, 595, 660])
        ecran.blit(self.image_croix, self.rect_croix)
        ecran.blit(self.texte, self.rect_texte)
        ecran.blit(self.image_fleche_droite, self.rect_fleche_droite)
        ecran.blit(self.image_fleche_gauche, self.rect_fleche_gauche)

        # gére la page qui est ouverte
        if self.page_utilise == 1:
            for item in self.item_page_1:
                ecran.blit(item.image, item.rect)

        # gére les clique de la sourit
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # aligné tout les elif ici

                if self.rect_croix.collidepoint(event.pos):
                    ecrire_log.ecrire_log(ecrire_log, " info : fermeture de l'atelier a batiment")
                    self.afichage_plus = "rien"
                    return False

                elif self.rect_fleche_gauche.collidepoint(event.pos):
                    if self.page_utilise != 1:
                        self.page_utilise -= 1
                    else:
                        self.page_utilise = self.max_page

                elif self.rect_fleche_droite.collidepoint(event.pos):
                    if self.page_utilise != self.max_page:
                        self.page_utilise += 1
                    else:
                        self.page_utilise = 1

                elif self.page_utilise == 1:
                    for item in self.item_page_1:
                        if item.rect.collidepoint(event.pos):
                            print("toucher")
                            self.afichage_plus = item.texte
                            self.prix_article = item.prix


                # si le bouton créé est cliqué
                if self.texte_achat_rect.collidepoint(event.pos):
                    self.choisir_creation()
        self.choisir_afichage()
        return True

    def creation_mine_niveau_2(self):
        self.nombre_fer = 0
        for i in range(10):
            if self.boite.verifie_puis_enlever(Item(190, "fer.....150", 30, 150)):
                self.nombre_fer += 1

        for i in range(20):
            if self.boite.verifie_puis_enlever(Item(440, "charbon......40", 30, 40)):
                self.nombre_charbon += 1

        if self.nombre_fer < 10:
            for i in range(self.nombre_fer):
                self.boite.items.append(Item(190, "fer.....150", 30, 150))
            for i in range(self.nombre_charbon):
                self.boite.items.append(Item(440, "charbon......40", 30, 40))
            self.nombre_fer = 0
            self.nombre_charbon = 0
            return False

        elif self.nombre_charbon < 20:
            for i in range(self.nombre_fer):
                self.boite.items.append(Item(190, "fer.....150", 30, 150))
            for i in range(self.nombre_charbon):
                self.boite.items.append(Item(440, "charbon......40", 30, 40))
            self.nombre_fer = 0
            self.nombre_charbon = 0
            return False

        if self.boite.verifie_puis_enlever(Item(240, "or.....500", 30, 500)):
            return True
        else:
            for i in range(self.nombre_fer):
                self.boite.items.append(Item(190, "fer.....150", 30, 150))
            for i in range(self.nombre_charbon):
                self.boite.items.append(Item(440, "charbon......40", 30, 40))
            self.nombre_fer = 0
            self.nombre_charbon = 0
            return False

    def choisir_afichage(self):
        if self.afichage_plus == "rien":
            self.afichage_plus = "rien"
        elif self.afichage_plus == "mine niveau 2":
            self.afichage_i1_p1()

    def choisir_creation(self):
        if self.afichage_plus == "rien":
            self.afichage_plus = "rien"
        elif self.afichage_plus == "mine niveau 2":
            self.afichage_plus = "rien"
            if self.creation_mine_niveau_2():
                print("ici c good")
                self.liste_batiment.append(Item(90, "mine niveau 2", 30, 0))

    def afichage_i1_p1(self):
        #ajouter 50 pour passer entre chaque premier ligne
        # [x;y du point un/x;y du point deux] pour le deuxiem y tu part a 30 et tu fais 50 en plus par texte
        self.texte_achat_rect.y = 290
        pygame.draw.rect(self.ecran, (255, 255, 255), [440, 115, 700, 230])
        self.ecran.blit(self.texte_i1_p1_P1, (450, 120))
        self.ecran.blit(self.texte_i1_p1_P2, (450, 160))
        self.ecran.blit(self.texte_i1_p1_P3, (450, 200))
        self.ecran.blit(self.texte_i1_p1_P4, (450, 240))
        self.ecran.blit(self.texte_achat, self.texte_achat_rect)