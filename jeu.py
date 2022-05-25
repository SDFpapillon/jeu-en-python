import pygame
import random
import math
from ecrire_log import  ecrire_log
from joueur import Joueur
from centrale_charbon import Centrale_charbon
from mine import Mine
from marche import Marche
from pousse_mais import Pousse_mais
from pousse_ble import Pousse_ble
from vache import Vache
from tourelle_1 import Tourelle_1
from dessalinisateu_niveau1 import dessalinisateur_niveau1
from boite_de_stocage import Boite_de_stocage
from item import Item
from monstre import Monstre
from atelier_batiment import Atelier_batiment
from mine_niveau_2 import Mine_niveau_2


#création classe de jeu
class Jeu:
    def __init__(self, ecran):
        self.atelier = False
        self.ecran = ecran
        self.atelier_batiment = Atelier_batiment()
        self.police = pygame.font.SysFont(pygame.font.get_fonts()[8], 20)
        self.police_texte = pygame.font.SysFont(pygame.font.get_fonts()[8], 30)
        self.nombre_item = -10
        self.item_utilise = "false"
        #sprite / lieu anexe
        self.joueur = Joueur()
        self.marche = Marche()
        self.centrale_charbon = Centrale_charbon()
        self.mine = Mine()
        self.mine_niveau_2 = Mine_niveau_2()
        self.mais = Pousse_mais()
        self.ble = Pousse_ble()
        self.vache = Vache()
        self.tourelle_1 = Tourelle_1()
        self.dessali1 = dessalinisateur_niveau1()
        self.boite_de_stocage = Boite_de_stocage()
        self.afichage_info = "false"
        self.presse = {}
        self.marche_afichage = False
        self.inventer_afichage = False
        self.boite_afiche = False
        self.atelier_batiment_afichage = False
        self.afichage_article = "rien"
        self.liste_batiment = []
        self.mouve_chose = self.joueur
        self.afichage_argent = self.police.render(str(self.joueur.argent), True, (0, 0, 0))
        self.compteur_temps = 0
        #afichage info batiment
        self.texte_produire = self.police_texte.render("- Produire", True, (0, 0, 0))
        self.texte_produire_rect = self.texte_produire.get_rect()
        self.texte_bouger = self.police_texte.render("- Déplacer", True, (0, 0, 0))
        self.texte_bouger_rect = self.texte_bouger.get_rect()
        self.texte_utilisation = self.police_texte.render("- Vendre la production", True, (0, 0, 0))
        self.texte_utilisation_rect = self.texte_utilisation.get_rect()
        self.afichage_info_batiment = False
        self.info_batiment = self.vache
        #monstre
        self.monstre = Monstre()
        self.tout_monstre = pygame.sprite.Group()
        self.attaque_en_cours = False

    def mouvement(self, chose):
        if self.presse.get(pygame.K_RIGHT):
            chose.MouvementDroite()
        elif self.presse.get(pygame.K_LEFT):
            chose.MouvementGauche()
        elif self.presse.get(pygame.K_UP):
            chose.MouvementHaut()
        elif self.presse.get(pygame.K_DOWN):
            chose.MouvementBas()

    def mise_A_jour(self, ecran):
        #ajouter compteur
        self.compteur_temps += 1
        #utilise le compteur pour produire automatiquement
        self.production_auto()
        # aficher image joueur
        ecran.blit(self.joueur.image, self.joueur.rect)
        #aficher les batiments
        self.afichage_batiment(ecran)
        #mettre a jour et aficher l'argent
        self.afichage_argent = self.police.render(str(self.joueur.argent), True, (0, 0, 0))
        ecran.blit(self.afichage_argent, (1000,10))
        #affichage bar de nouriture et eau
        pygame.draw.rect(ecran, (88, 41, 0), [1070, 0, 10, self.joueur.nouriture * 2])
        pygame.draw.rect(ecran, (0, 0, 128), [1060, 0, 10, self.joueur.eau * 2])
        #bouger le joueur / batiment selectionner
        self.mouvement(self.mouve_chose)
        #diminuer la nouriture du joueur et de l'eau
        self.joueur.nouriture -= 0.01
        self.joueur.eau -= 0.01
        #tué le joueur en cas de faim/soife trop faible
        if self.joueur.eau < 0:
            self.joueur.mourir()
        if self.joueur.nouriture < 0:
            self.joueur.mourir()

        if self.marche_afichage:
            self.marche_MAJ(ecran)
        if self.inventer_afichage:
            self.MAJ_inventer(ecran)
        if self.boite_afiche:
            self.boite(ecran)
        if self.atelier_batiment_afichage:
            if not self.atelier_batiment.afichage_etablie(self.ecran, self.boite_de_stocage, self.liste_batiment):
                self.atelier_batiment_afichage = False

        if self.afichage_info_batiment:
            self.info_sup_batiment(ecran, self.info_batiment)

        if self.attaque_en_cours:
            self.attaque(self.ecran)

        self.touche_clavier()

    def touche_clavier(self):
        if not self.attaque_en_cours:
            if self.presse.get(pygame.K_m):
                self.presse[pygame.K_m] = False
                self.marche_afichage = True
                ecrire_log.ecrire_log(self=ecrire_log, texte=" info : afichage du marcher")
            elif self.presse.get(pygame.K_p):
                if self.joueur.verif_inventair("cannne a peche.......50"):
                    self.peche()
            elif self.presse.get(pygame.K_i):
                self.presse[pygame.K_i] = False
                self.inventer_afichage = True
                ecrire_log.ecrire_log(self=ecrire_log, texte=" info : affichage inventaire")
            elif self.presse.get(pygame.K_b):
                self.presse[pygame.K_b] = False
                self.boite_afiche = True
                ecrire_log.ecrire_log(self=ecrire_log, texte=" info : affichage boite")
            elif self.presse.get(pygame.K_SPACE):
                self.mouve_chose = self.joueur
            elif self.presse.get(pygame.K_c):
                cantite_batiment = 0
                for batiment in self.liste_batiment:
                    if batiment.texte == self.joueur.batiment_liste[0]:
                        cantite_batiment += random.randint(1, 5)
                    if batiment.texte == self.joueur.batiment_liste[1]:
                        cantite_batiment += random.randint(1, 5)
                    if batiment.texte == self.joueur.batiment_liste[2]:
                        cantite_batiment += random.randint(1, 5)
                    if batiment.texte == self.joueur.batiment_liste[3]:
                        cantite_batiment += random.randint(1, 5)
                    if batiment.texte == self.joueur.batiment_liste[4]:
                        cantite_batiment += random.randint(1, 5)
                self.cree_les_monstre(random.randint(10, 15) + cantite_batiment)
                for monstre in self.tout_monstre:
                    monstre.vitesse = random.randint(1, 3)
                self.attaque_en_cours = True
            elif self.presse.get(pygame.K_v):
                print("ok")
                self.presse[pygame.K_v] = False
                if self.atelier:
                    print("c bon")
                    self.atelier_batiment_afichage = True
            if self.presse.get(pygame.K_g):
                if self.presse.get(pygame.K_a):
                    if self.presse.get(pygame.K_p):
                        if self.presse.get(pygame.K_x):
                            if self.presse.get(pygame.K_o):
                                self.triche()

        else:
            if self.presse.get(pygame.K_SPACE):
                ecrire_log.ecrire_log(self=ecrire_log, texte=" info : attaque comencer")
                self.joueur.attaque(self.tout_monstre)
                self.tuer_les_monstre_mort()
                self.revenir_a_la_normal()

    def triche(self):
        self.joueur.argent = 10000
        self.joueur.nouriture = 0
        self.joueur.eau = 0
        self.joueur.je_peux_mourir = False
        self.atelier = True
        self.dessali1.rect.y = 90
        self.dessali1.rect.x = 40
        self.liste_batiment.append(Item(0, "dessalinisateur niveau 1........70", 30, 70))
        self.vache.rect.y = 90
        self.vache.rect.x = 90
        self.liste_batiment.append(Item(0, "vache.......180", 30, 180))
        self.mine.rect.y = 90
        self.mine.rect.x = 140
        self.liste_batiment.append(Item(0, "mine.......10000", 30, 70))
        self.mais.rect.y = 90
        self.mais.rect.x = 190
        self.liste_batiment.append(Item(0, "pousse de maïs......50", 30, 70))
        self.ble.rect.y = 90
        self.ble.rect.x = 240
        self.liste_batiment.append(Item(0, "pousse de blé......90", 30, 70))
        self.mine_niveau_2.rect.y = 140
        self.mine_niveau_2.rect.x = 90
        self.liste_batiment.append(Item(0, "mine niveau 2", 30, 70))
        self.centrale_charbon.rect.y = 140
        self.centrale_charbon.rect.x = 140
        self.liste_batiment.append(Item(0, "centrale au charbon.....6000", 30, 70))
        self.tourelle_1.rect.y = 140
        self.tourelle_1.rect.x = 190
        self.liste_batiment.append(Item(0, "tourelle de combat....450", 30, 70))
        for batiment in self.liste_batiment:
            batiment.produire_ou = "boite"

    def boite(self, ecran):
        self.boite_de_stocage.MAJ_nombre_pages()
        self.boite_de_stocage.MAJ_des_items()
        pygame.draw.rect(ecran, (255, 255, 255), [240, 20, 595, 660])
        ecran.blit(self.boite_de_stocage.texte, self.boite_de_stocage.rect_texte)
        ecran.blit(self.boite_de_stocage.image_fleche_droite, self.boite_de_stocage.rect_fleche_droite)
        ecran.blit(self.boite_de_stocage.image_fleche_gauche, self.boite_de_stocage.rect_fleche_gauche)
        ecran.blit(self.boite_de_stocage.image_croix, self.boite_de_stocage.rect_croix)
        for item in self.boite_de_stocage.items:
            ecran.blit(item.image, item.rect)
        for item in self.boite_de_stocage.items:
            if self.afichage_info == item.texte:
                self.item_utilise = item
                self.nombre_item = item
                pygame.draw.rect(ecran, (0, 200, 200), [0, 0, 200, 200])
                ecran.blit(item.image, (0, 10))
                ecran.blit(self.boite_de_stocage.texte_vendre, self.boite_de_stocage.rect_vendre)
                ecran.blit(self.boite_de_stocage.texte_inventaire, self.boite_de_stocage.rect_inventaire)
        # gére les evenemetn clique de la sourit + touche clavier
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.boite_de_stocage.rect_croix.collidepoint(event.pos):
                    self.boite_afiche = False
                elif self.boite_de_stocage.rect_fleche_droite.collidepoint(event.pos):
                    self.boite_de_stocage.page_up()
                elif self.boite_de_stocage.rect_fleche_gauche.collidepoint(event.pos):
                    self.boite_de_stocage.page_down()
                elif self.boite_de_stocage.rect_inventaire.collidepoint(event.pos):
                    self.boite_de_stocage.deplace_inventaire(self.joueur, self.item_utilise)
                elif self.boite_de_stocage.rect_vendre.collidepoint(event.pos):
                    self.joueur.argent += int(self.item_utilise.prix) /2
                    self.boite_de_stocage.items.remove(self.item_utilise)
                for item in self.boite_de_stocage.items:
                    if item.rect.collidepoint(event.pos):
                        self.afichage_info = item.texte

            elif event.type == pygame.KEYDOWN:
                self.presse[event.key] = True

            elif event.type == pygame.KEYUP:
                self.presse[event.key] = False
        if self.presse.get(pygame.K_v):
            self.joueur.argent += int(self.item_utilise.prix) / 2
            self.boite_de_stocage.items.remove(self.item_utilise)

    def MAJ_inventer(self, ecran):
        pygame.draw.rect(ecran, (255, 255, 255), [240, 20, 595, 660])
        ecran.blit(self.joueur.texte, self.joueur.rect_texte)
        ecran.blit(self.joueur.image_croix_joueur, self.joueur.rect_croix_joueur)
        for item in range(1,11):
            ecran.blit(self.joueur.inventer[item].image, self.joueur.inventer[item].rect)
        for item in range(1,11):
            if self.afichage_info == self.joueur.inventer[item].texte:
                self.item_utilise = self.joueur.inventer[item]
                self.nombre_item = item
                pygame.draw.rect(ecran, (0, 200, 200), [0, 0, 200, 200])
                ecran.blit(self.joueur.inventer[item].image, (0, 10))
                ecran.blit(self.joueur.texte_utilise, self.joueur.rect_utilise)
                ecran.blit(self.joueur.texte_vendre, self.joueur.rect_vendre)
                ecran.blit(self.joueur.texte_boite, self.joueur.rect_boite)

        # gére les clique de la sourit
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.joueur.rect_croix_joueur.collidepoint(event.pos):
                    self.inventer_afichage = False
                    self.afichage_info = "false"#valeur non utilisé
                elif self.joueur.rect_boite.collidepoint(event.pos):
                    self.boite_de_stocage.items.append(self.joueur.inventer[self.nombre_item])
                    self.joueur.enlever_item(self.nombre_item, self.joueur.inventer[self.nombre_item].rect.y)
                    self.afichage_info = "false"
                elif self.joueur.rect_vendre.collidepoint(event.pos):
                    self.joueur.argent += self.joueur.inventer[self.nombre_item].prix / 2
                    self.joueur.enlever_item(self.nombre_item, self.joueur.inventer[self.nombre_item].rect.y)
                    self.afichage_info = "false"
                elif self.joueur.rect_utilise.collidepoint(event.pos):
                    if self.choisir_utilisation(self.joueur.inventer[self.nombre_item]):
                        self.joueur.enlever_item(self.nombre_item, self.joueur.inventer[self.nombre_item].rect.y)
                    self.afichage_info = "false"
                for item in self.joueur.inventer:
                    if self.joueur.inventer[item].rect.collidepoint(event.pos):
                        self.afichage_info = self.joueur.inventer[item].texte

            elif event.type == pygame.KEYDOWN:
                self.presse[event.key] = True

            elif event.type == pygame.KEYUP:
                self.presse[event.key] = False

        if self.afichage_info != "false":
            if self.presse.get(pygame.K_v):
                self.afichage_info = "false"
                self.presse[pygame.K_v] = False
                self.joueur.argent += self.joueur.inventer[self.nombre_item].prix / 2
                self.joueur.enlever_item(self.nombre_item, self.joueur.inventer[self.nombre_item].rect.y)
            elif self.presse.get(pygame.K_q):
                self.afichage_info = "false"
                self.presse[pygame.K_q] = False
                self.boite_de_stocage.items.append(self.joueur.inventer[self.nombre_item])
                self.joueur.enlever_item(self.nombre_item, self.joueur.inventer[self.nombre_item].rect.y)
            elif self.presse.get(pygame.K_u):
                self.afichage_info = "false"
                self.presse[pygame.K_u] = False
                if self.choisir_utilisation(self.joueur.inventer[self.nombre_item]):
                    self.joueur.enlever_item(self.nombre_item, self.joueur.inventer[self.nombre_item].rect.y)

    def choisir_utilisation(self,item):
        print(item.texte)
        if item.texte == "atelier a batiment....1000":
            print("ici ok")
            self.atelier = True
            return True
        if item.texte in self.joueur.nouriture_liste:
            self.joueur.add_nouriture(item)
            return True
        elif item.texte in self.joueur.batiment_liste:
            self.liste_batiment.append(item)
            if item.texte == self.joueur.batiment_liste[0]:
                self.mouve_chose = self.dessali1
            if item.texte == self.joueur.batiment_liste[1]:
                self.mouve_chose = self.mais
            if item.texte == self.joueur.batiment_liste[2]:
                self.mouve_chose = self.ble
            if item.texte == self.joueur.batiment_liste[3]:
                self.mouve_chose = self.vache
            if item.texte == self.joueur.batiment_liste[4]:
                self.mouve_chose = self.tourelle_1
            if item.texte == self.joueur.batiment_liste[5]:
                self.mouve_chose = self.centrale_charbon
            if item.texte == self.joueur.batiment_liste[6]:
                self.mouve_chose = self.mine

            return True
        else:
            return False

    def peche(self):
        resulta_peche = random.randint(1, 1001)
        if resulta_peche < 900:
            self.joueur.ajoute_inventer("poisson.......10", 10)
        elif resulta_peche < 999:
            self.joueur.ajoute_inventer("poisson moyen", 15)
        else:
            self.joueur.ajoute_inventer("mega poisson", 20)

    def marche_MAJ(self,ecran):
        pygame.draw.rect(ecran, (255, 255, 255), [240, 20, 595, 660])
        ecran.blit(self.marche.image_croix, self.marche.rect_croix)
        ecran.blit(self.marche.texte, self.marche.rect_texte)
        ecran.blit(self.marche.image_fleche_droite, self.marche.rect_fleche_droite)
        ecran.blit(self.marche.image_fleche_gauche, self.marche.rect_fleche_gauche)

        #gére la page qui est ouverte
        if self.marche.page_utilise == 1:
            for item in self.marche.items_page_1:
                ecran.blit(item.image, item.rect)

        elif self.marche.page_utilise == 2:
            for item in self.marche.items_page_2:
                ecran.blit(item.image, item.rect)

        elif self.marche.page_utilise == 3:
            for item in self.marche.items_page_3:
                ecran.blit(item.image, item.rect)

        #gére les clique de la sourit
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #aligné tout les elif ici

                if self.marche.rect_croix.collidepoint(event.pos):
                    ecrire_log.ecrire_log(self=ecrire_log, texte=" info : fermeture du marcher")
                    self.marche_afichage = False
                    self.afichage_article = "rien"

                elif self.marche.rect_fleche_gauche.collidepoint(event.pos):
                    if self.marche.page_utilise != 1:
                        self.marche.page_utilise -= 1
                    else:
                        self.marche.page_utilise = self.marche.max_page

                elif self.marche.rect_fleche_droite.collidepoint(event.pos):
                    if self.marche.page_utilise != self.marche.max_page:
                        self.marche.page_utilise += 1
                    else:
                        self.marche.page_utilise = 1

                elif self.marche.page_utilise == 1:
                    for item in self.marche.items_page_1:
                        if item.rect.collidepoint(event.pos):
                            self.afichage_article = item.texte
                            self.prix_article = item.prix

                elif self.marche.page_utilise == 2:
                    for item in self.marche.items_page_2:
                        if item.rect.collidepoint(event.pos):
                            self.afichage_article = item.texte
                            self.prix_article = item.prix
                elif self.marche.page_utilise == 3:
                    for item in self.marche.items_page_3:
                        if item.rect.collidepoint(event.pos):
                            self.afichage_article = item.texte
                            self.prix_article = item.prix

                  #si le bouton achat est cliqué
                if self.marche.texte_achat_rect.collidepoint(event.pos):
                    if self.prix_article <= self.joueur.argent:
                        self.joueur.argent -= self.prix_article
                        for item in self.joueur.inventer:
                            if self.joueur.inventer[item].texte == "rien":
                                self.joueur.inventer[item] = Item(self.joueur.inventer[item].rect.y, self.afichage_article, 30, self.prix_article)
                                break
                        self.afichage_article = "rien"

        # gére l'afichage de l'article sélectionné
        if self.afichage_article == "dessalinisateur niveau 1........70":
            self.marche.afichage_i1_p1(ecran)
        elif self.afichage_article == "cannne a peche.......50":
            self.marche.afichage_i2_p1(ecran)
        elif self.afichage_article == "poisson.......10":
            self.marche.afichage_i3_p1(ecran)
        elif self.afichage_article == "gros poisson.......20":
            self.marche.afichage_i4_p1(ecran)
        elif self.afichage_article == "pousse de maïs......50":
            self.marche.afichage_i5_p1(ecran)
        elif self.afichage_article == "maïs......10":
            self.marche.afichage_i6_p1(ecran)
        elif self.afichage_article == "poulet cuit........30":
            self.marche.afichage_i7_p1(ecran)
        elif self.afichage_article == "pain.......30":
            self.marche.afichage_i8_p1(ecran)
        elif self.afichage_article == "1 litre d'eau........10":
            self.marche.afichage_i9_p1(ecran)
        elif self.afichage_article == "vache.......180":
            self.marche.afichage_i10_p1(ecran)
        elif self.afichage_article == "pousse de blé......90":
            self.marche.afichage_i1_p2(ecran)
        elif self.afichage_article == "blé.....20":
            self.marche.afichage_i2_p2(ecran)
        elif self.afichage_article == "1 litre de lait......40":
            self.marche.afichage_i3_p2(ecran)
        elif self.afichage_article == "arc........140":
            self.marche.afichage_i4_p2(ecran)
        elif self.afichage_article == "ficelle.......30":
            self.marche.afichage_i5_p2(ecran)
        elif self.afichage_article == "tourelle de combat....450":
            self.marche.afichage_i6_p2(ecran)
        elif self.afichage_article == "centrale au charbon.....6000":
            self.marche.afichage_i7_p2(ecran)
        elif self.afichage_article == "charbon......40":
            self.marche.afichage_i8_p2(ecran)
        elif self.afichage_article == "mine.......10000":
            self.marche.afichage_i9_p2(ecran)
        elif self.afichage_article == "électricité......10":
            self.marche.afichage_i10_p2(ecran)
        elif self.afichage_article == "mousquet......500":
            self.marche.afichage_i1_p3(ecran)
        elif self.afichage_article == "cuivre.....100":
            self.marche.afichage_i2_p3(ecran)
        elif self.afichage_article == "fer.....150":
            self.marche.afichage_i3_p3(ecran)
        elif self.afichage_article == "or.....500":
            self.marche.afichage_i4_p3(ecran)
        elif self.afichage_article == "diamant....1000":
            self.marche.afichage_i5_p3(ecran)
        elif self.afichage_article == "atelier a batiment....1000":
            self.marche.afichage_i6_p3(ecran)

    def production_auto(self):
        if self.compteur_temps % 100 == 0:
            if self.dessali1.rect.y > 0:
                self.boite_de_stocage.items.append(Item(0, "1 litre d'eau........10", 30, 10))
            if self.attaque_en_cours:
                if self.tourelle_1.rect.y > 0:
                    self.tourelle_1.attaquer_les_monstres(self)
                    self.tuer_les_monstre_mort()
                    self.revenir_a_la_normal()
        if self.compteur_temps % 400 == 0:
            if self.vache.rect.y > 0:
                self.vache.produire(self.joueur, self.boite_de_stocage)
            if self.ble.rect.y > 0:
                self.ble.produire(self.joueur, self.boite_de_stocage)
            if self.mais.rect.y > 0:
                self.mais.produire(self.joueur, self.boite_de_stocage)
            if self.mine.rect.y > 0:
                self.mine.produire(self.joueur, self.boite_de_stocage)
            if self.mine_niveau_2.rect.y > 0:
                self.mine_niveau_2.produire(self.joueur, self.boite_de_stocage)

    def afichage_batiment(self, ecran):
        for batiment in self.liste_batiment:
            if batiment.texte == self.joueur.batiment_liste[0]:
                ecran.blit(self.dessali1.image, self.dessali1.rect)
            if batiment.texte == self.joueur.batiment_liste[1]:
                ecran.blit(self.mais.image, self.mais.rect)
            if batiment.texte == self.joueur.batiment_liste[2]:
                ecran.blit(self.ble.image, self.ble.rect)
            if batiment.texte == self.joueur.batiment_liste[3]:
                ecran.blit(self.vache.image, self.vache.rect)
            if batiment.texte == self.joueur.batiment_liste[4]:
                ecran.blit(self.tourelle_1.image, self.tourelle_1.rect)
            if batiment.texte == self.joueur.batiment_liste[5]:
                ecran.blit(self.centrale_charbon.image, self.centrale_charbon.rect)
            if batiment.texte == self.joueur.batiment_liste[6]:
                ecran.blit(self.mine.image, self.mine.rect)
            if batiment.texte == self.joueur.batiment_liste[7]:
                ecran.blit(self.mine_niveau_2.image, self.mine_niveau_2.rect)

    def info_sup_batiment(self, ecran, batiment):
        ecrire_log.ecrire_log(ecrire_log, " information suplementaire aficher")
        self.texte_bouger_rect.y = batiment.rect.y + 10
        self.texte_bouger_rect.x = batiment.rect.x + 60
        self.texte_produire_rect.y = batiment.rect.y + 60
        self.texte_produire_rect.x = batiment.rect.x + 60
        self.texte_utilisation_rect.y = batiment.rect.y + 110
        self.texte_utilisation_rect.x =batiment.rect.x + 60
        pygame.draw.rect(ecran, (255, 255, 255), [batiment.rect.x + 50,batiment.rect.y, 240, 160])
        ecran.blit(self.texte_produire, self.texte_produire_rect)
        ecran.blit(self.texte_bouger, self.texte_bouger_rect)
        ecran.blit(self.texte_utilisation, self.texte_utilisation_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.texte_bouger_rect.collidepoint(event.pos):
                    self.mouve_chose = batiment
                    self.afichage_info_batiment = False
                elif self.texte_produire_rect.collidepoint(event.pos):
                    batiment.produire_ou = "joueur"
                    batiment.produire(self.joueur, self.boite_de_stocage)
                elif self.texte_utilisation_rect.collidepoint(event.pos):
                    if batiment.produire_ou == "boite":
                        batiment.produire_ou = "vendre"
                        self.texte_utilisation = self.police_texte.render("- Vendre la production", True, (0, 0, 0))
                    else:
                        batiment.produire_ou = "boite"
                        self.texte_utilisation = self.police_texte.render("- Mettre en boite la production", True, (0, 0, 0))

    def cree_les_monstre(self, nombre_monstre):
        ecrire_log.ecrire_log(ecrire_log, " création des monstres")
        for i in range(nombre_monstre):
            self.tout_monstre.add(Monstre())

        for monstre in self.tout_monstre:
            monstre.rect.x = random.randint(0,650)
            monstre.rect.y = random.randint(0, 1030)

    def attaque(self, ecran):
        ecrire_log.ecrire_log(ecrire_log, " attaque")
        self.tout_monstre.draw(ecran)
        for monstre in self.tout_monstre:
            if self.joueur.rect.x > monstre.rect.x:
                monstre.rect.x += monstre.vitesse
            if self.joueur.rect.x < monstre.rect.x:
                monstre.rect.x -= monstre.vitesse
            if self.joueur.rect.y > monstre.rect.y:
                monstre.rect.y += monstre.vitesse
            if self.joueur.rect.y < monstre.rect.y:
                monstre.rect.y -= monstre.vitesse
            monstre.distance_joueur = self.rect_distance(monstre.rect, self.joueur.rect)
            if monstre.distance_joueur == 0:
                self.joueur.nouriture -= 1
            monstre.bar_de_vie(self.ecran)

    def rect_distance(self, rect1, rect2):
        x1, y1 = rect1.topleft
        x1b, y1b = rect1.bottomright
        x2, y2 = rect2.topleft
        x2b, y2b = rect2.bottomright
        left = x2b < x1
        right = x1b < x2
        top = y2b < y1
        bottom = y1b < y2
        if bottom and left:
            return math.hypot(x2b - x1, y2 - y1b)
        elif left and top:
            return math.hypot(x2b - x1, y2b - y1)
        elif top and right:
            return math.hypot(x2 - x1b, y2b - y1)
        elif right and bottom:
            return math.hypot(x2 - x1b, y2 - y1b)
        elif left:
            return x1 - x2b
        elif right:
            return x2 - x1b
        elif top:
            return y1 - y2b
        elif bottom:
            return y2 - y1b
        else:  # rectangles intersect
            return 0

    def tuer_les_monstre_mort(self):
        ecrire_log.ecrire_log(ecrire_log, " monstres meurts")
        for monstre in self.tout_monstre:
            if monstre.vie <= 0:
                self.tout_monstre.remove(monstre)
                self.joueur.argent += random.randint(10, 30)

    def revenir_a_la_normal(self):
        ecrire_log.ecrire_log(ecrire_log, "retoure a la normal")
        if 0 == len(self.tout_monstre):
            self.attaque_en_cours = False
            ecrire_log.ecrire_log(self=ecrire_log, texte=" info : attaque finit")
