import pygame
from item import Item

class Marche(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.page_utilise = 1
        self.max_page = 3
        self.police = pygame.font.SysFont(pygame.font.get_fonts()[8], 40)
        self.image_croix = pygame.image.load('image/croix.jpg')
        self.image_croix = pygame.transform.scale(self.image_croix, (50, 50))
        self.rect_croix = self.image_croix.get_rect()
        self.rect_croix.x = 765
        self.rect_croix.y = 20
        self.prix_objet = 0
        self.type_objet = "rien"
        #fléche page +/-
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
        #texte marché
        self.police_texte = pygame.font.SysFont(pygame.font.get_fonts()[8], 70)
        self.texte = self.police_texte.render("marché", True, (0, 0, 0))
        self.rect_texte = self.texte.get_rect()
        self.rect_texte.x = 250
        self.rect_texte.y = 30
        self.items_page_3 = [
            Item(90, "mousquet......500", 30, 500),
            Item(140, "cuivre.....100", 30, 100),
            Item(190, "fer.....150", 30, 150),
            Item(240, "or.....500", 30, 500),
            Item(290, "diamant....1000", 30, 1000),
            Item(340, "atelier a batiment....1000", 30, 1000),
        ]
        self.items_page_2 = [
            # Item(y, texte, taille police, prix)
            Item(90, "pousse de blé......90", 30, 90),
            Item(140, "blé.....20", 30, 20),
            Item(190, "1 litre de lait......40", 30, 40),
            Item(240, "arc........140", 30, 140),
            Item(290, "ficelle.......30", 30, 30),
            Item(340, "tourelle de combat....450", 30, 450),
            Item(390, "centrale au charbon.....6000", 30, 6000),
            Item(440, "charbon......40", 30, 40),
            Item(490, "mine.......10000", 30, 10000),
            Item(540, "électricité......10", 30, 10)
        ]
        self.items_page_1 = [
           #Item(y, texte, taille police, prix)
            Item(90, "dessalinisateur niveau 1........70", 30, 70),
            Item(140, "cannne a peche.......50", 30, 50),
            Item(190, "poisson.......10", 30, 10),
            Item(240, "gros poisson.......20", 30, 20),
            Item(290, "pousse de maïs......50",30, 50),
            Item(340, "maïs......10", 30, 10),
            Item(390, "poulet cuit........30", 30, 30),
            Item(440, "pain.......30", 30, 30),
            Item(490, "1 litre d'eau........10", 30, 10),
            Item(540, "vache.......180", 30, 180)
        ]



        #texte de description des item + page corespondande le P corespon a la partie du texte i desigle l'item et p la page
        self.police_article = pygame.font.SysFont(pygame.font.get_fonts()[8], 30)
        self.texte_achat = self.police_article.render("ACHETER", True, (0, 128, 0))
        self.texte_achat_rect = self.texte_achat.get_rect()
        self.texte_achat_rect.x = 550
        #texte i1-10 p1
        self.texte_i1_p1_P1 = self.police_article.render("Le dessalinisateur niveau 1 permet de transformé", True, (0, 0, 0))
        self.texte_i1_p1_P2 = self.police_article.render("jusqu'à deux litre deux de mer en eau potable par jour. ", True, (0, 0, 0))
        self.texte_i1_p1_P3 = self.police_article.render("Cependant il n'essecite l'intervention humaine pour le ramplire.", True, (0, 0, 0))
        self.texte_i2_p1_P1 = self.police_article.render("La canne a peche permet de pecher du poisson. pour l'utiliser ", True,(0, 0, 0))
        self.texte_i2_p1_P2 = self.police_article.render("appuyer sur la touche p ",True, (0, 0, 0))
        self.texte_i2_p1_P3 = self.police_article.render("Pourcentage de chance de caque poisson: ", True, (0, 0, 0))
        self.texte_i2_p1_P4 = self.police_article.render("Petit --> 90%; moyen --> 9,9%; gros --> 0,1% ", True, (0, 0, 0))
        self.texte_i3_p1_P1 = self.police_article.render("Le poisson est une source de nouriture. Il s'opptien en péchent ", True, (0, 0, 0))
        self.texte_i4_p1_P1 = self.police_article.render("Le gros poisson est une vertion amélioré du poisson. Il nourit ", True, (0, 0, 0))
        self.texte_i4_p1_P2 = self.police_article.render("plus mais coute plus cher.",True, (0, 0, 0))
        self.texte_i5_p1_P1 = self.police_article.render("la pousse de maïs permet de produire du maïs. Le maïs peut être", True, (0, 0, 0))
        self.texte_i5_p1_P2 = self.police_article.render("vendu ou comsomé.", True, (0, 0, 0))
        self.texte_i6_p1_P1 = self.police_article.render("Le maïs peut servire s'alimentation pour le joueur ou pour la ", True, (0, 0, 0))
        self.texte_i6_p1_P2 = self.police_article.render("vache. Il peut aussi être vendue. Il est produit par la pousse", True, (0, 0, 0))
        self.texte_i6_p1_P3 = self.police_article.render("de maïs.", True, (0, 0, 0))
        self.texte_i7_p1_P1 = self.police_article.render("Le poulet cuit ne peux pas être produit. Cepandant il raporte", True, (0, 0, 0))
        self.texte_i7_p1_P2 = self.police_article.render("beaucoup de nouriture.", True, (0, 0, 0))
        self.texte_i8_p1_P1 = self.police_article.render("Le pain peut être fabriqué a partire d'eau et de blé. Il se", True, (0, 0, 0))
        self.texte_i8_p1_P2 = self.police_article.render("créé dans le four(sera disponible a la prochaine MAJ). Le ", True, (0, 0, 0))
        self.texte_i8_p1_P3 = self.police_article.render("pain raporte énormément de nouriture.", True, (0, 0, 0))
        self.texte_i9_p1_P1 = self.police_article.render("L'eau est un élément essenciel a la survie elle ne peut se",True, (0, 0, 0))
        self.texte_i9_p1_P2 = self.police_article.render("procuré avec un dessalinisateur. Elle permet de faire ",True, (0, 0, 0))
        self.texte_i9_p1_P3 = self.police_article.render("pousser les plante, faire boire les animaux et boire.", True, (0, 0, 0))
        self.texte_i10_p1_P1 = self.police_article.render("La vache est un batiment qui produit du lait. ",True, (0, 0, 0))
        self.texte_i10_p1_P2 = self.police_article.render("Elle demande de l'eau et du blé pour faire du lait.",True, (0, 0, 0))
        #i1-10 p2
        self.texte_i1_p2_P1 = self.police_article.render("La pousse de blé permet de produire du blé en consoment",True, (0, 0, 0))
        self.texte_i1_p2_P2 = self.police_article.render("de l'eau", True, (0, 0, 0))
        self.texte_i2_p2_P1 = self.police_article.render("Le blé est une source de nouriture. Dans une prochaine", True, (0, 0, 0))
        self.texte_i2_p2_P2 = self.police_article.render("MAJ il servira a faire du pain.", True, (0, 0, 0))
        self.texte_i3_p2_P1 = self.police_article.render("Le lait est une source d'alimentation qui permet de ", True, (0, 0, 0))
        self.texte_i3_p2_P2 = self.police_article.render("s'hydrater et de se nourrir.", True, (0, 0, 0))
        self.texte_i4_p2_P1 = self.police_article.render("L'arc permet de combatre les monstre. Il fait plus de", True, (0, 0, 0))
        self.texte_i4_p2_P2 = self.police_article.render("degat et permet d'attaquer a distence.", True, (0, 0, 0))
        self.texte_i5_p2_P1 = self.police_article.render("La ficelle pouras être utilisé pour créé une tante dans une", True, (0, 0, 0))
        self.texte_i5_p2_P2 = self.police_article.render("des prochaine MAJ.", True, (0, 0, 0))
        self.texte_i6_p2_P1 = self.police_article.render("La tourlle de combat se comporte comme un batiment mais elle", True, (0, 0, 0))
        self.texte_i6_p2_P2 = self.police_article.render("attaque les monstres a proximiter.", True, (0, 0, 0))
        self.texte_i7_p2_P1 = self.police_article.render("La centrale au charbon utilise du charbon pour produire de ",True, (0, 0, 0))
        self.texte_i7_p2_P2 = self.police_article.render("l'éléctricité.",True, (0, 0, 0))
        self.texte_i8_p2_P1 = self.police_article.render("Le charbon est une ressource de base pour preduire de",True, (0, 0, 0))
        self.texte_i8_p2_P2 = self.police_article.render("l'éléctricité. Il est peux cher et permet une production",True, (0, 0, 0))
        self.texte_i8_p2_P3 = self.police_article.render("a faible cout.",True, (0, 0, 0))
        self.texte_i9_p2_P1 = self.police_article.render("La mine permet de produire des minerais, pour l'instant",True, (0, 0, 0))
        self.texte_i9_p2_P2 = self.police_article.render("que du charbon mais elle produira ensuite du fer de l'or...",True, (0, 0, 0))
        self.texte_i10_p2_P1 = self.police_article.render("L'éléctricité est une ressource de base pour les machine ",True, (0, 0, 0))
        self.texte_i10_p2_P2 = self.police_article.render("avencer.",True, (0, 0, 0))
        #i1-10 p3
        self.texte_i1_p3_P1 = self.police_article.render("Le mousquet est un fusille a faible cadence de tire mais il", True, (0, 0, 0))
        self.texte_i1_p3_P2 = self.police_article.render("fait beaucoup de dégat.", True, (0, 0, 0))
        self.texte_i2_p3_P1 = self.police_article.render("Le cuivre est un élément de base pour faire de l'electronique", True, (0, 0, 0))
        self.texte_i2_p3_P2 = self.police_article.render("il est produit par la mine.", True, (0, 0, 0))
        self.texte_i3_p3_P1 = self.police_article.render("Le fer est un élément permetent la construction d'arme et de", True, (0, 0, 0))
        self.texte_i3_p3_P2 = self.police_article.render("batiment avancer. Il est produit dans la mine.", True, (0, 0, 0))
        self.texte_i4_p3_P1 = self.police_article.render("L'or est un minerais rare qui permet de faire des circuts", True, (0, 0, 0))
        self.texte_i4_p3_P2 = self.police_article.render("electrique de très haute pressision.", True, (0, 0, 0))
        self.texte_i5_p3_P1 = self.police_article.render("Le diamant est un minerais d'une extrème rareté il est utiliser", True, (0, 0, 0))
        self.texte_i5_p3_P2 = self.police_article.render("pour faire des lentille pour les armes laser.", True, (0, 0, 0))

        self.texte_i6_p3_P1 = self.police_article.render("L'atelier a batiment permet de créé des batiments de niveau", True, (0, 0, 0))
        self.texte_i6_p3_P2 = self.police_article.render("plus élever. Il peut s'ouvrire en appuyent sur V",True, (0, 0, 0))

    def afichage_i1_p1(self, ecran):
        #ajouter 50 pour passer entre chaque premier ligne
        # [x;y du point un/x;y du point deux] pour le deuxiem y tu part a 30 et tu fais 50 en plus par texte
        self.texte_achat_rect.y = 250
        pygame.draw.rect(ecran, (255, 255, 255), [440, 115, 700, 180])
        ecran.blit(self.texte_i1_p1_P1, (450, 120))
        ecran.blit(self.texte_i1_p1_P2, (450, 160))
        ecran.blit(self.texte_i1_p1_P3, (450, 200))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i2_p1(self, ecran):
        self.texte_achat_rect.y = 340
        pygame.draw.rect(ecran, (255, 255, 255), [440, 165, 700, 200])
        ecran.blit(self.texte_i2_p1_P1, (450, 170))
        ecran.blit(self.texte_i2_p1_P2, (450, 210))
        ecran.blit(self.texte_i2_p1_P3, (450, 250))
        ecran.blit(self.texte_i2_p1_P4, (450, 290))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i3_p1(self, ecran):
        self.texte_achat_rect.y = 250
        pygame.draw.rect(ecran, (255, 255, 255), [440, 215, 700, 80])
        ecran.blit(self.texte_i3_p1_P1, (450, 220))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i4_p1(self, ecran):
        self.texte_achat_rect.y = 360
        pygame.draw.rect(ecran, (255, 255, 255), [440, 265, 700, 130])
        ecran.blit(self.texte_i4_p1_P1, (450, 270))
        ecran.blit(self.texte_i4_p1_P2, (450, 310))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i5_p1(self, ecran):
        self.texte_achat_rect.y = 410
        pygame.draw.rect(ecran, (255, 255, 255), [440, 315, 700, 130])
        ecran.blit(self.texte_i5_p1_P1, (450, 320))
        ecran.blit(self.texte_i5_p1_P2, (450, 360))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i6_p1(self, ecran):
        self.texte_achat_rect.y = 500
        pygame.draw.rect(ecran, (255, 255, 255), [440, 365, 700, 180])
        ecran.blit(self.texte_i6_p1_P1, (450, 370))
        ecran.blit(self.texte_i6_p1_P2, (450, 410))
        ecran.blit(self.texte_i6_p1_P3, (450, 450))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i7_p1(self, ecran):
        self.texte_achat_rect.y = 510
        pygame.draw.rect(ecran, (255, 255, 255), [440, 415, 700, 130])
        ecran.blit(self.texte_i7_p1_P1, (450, 420))
        ecran.blit(self.texte_i7_p1_P2, (450, 460))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i8_p1(self, ecran):
        self.texte_achat_rect.y = 600
        pygame.draw.rect(ecran, (255, 255, 255), [440, 465, 700, 180])
        ecran.blit(self.texte_i8_p1_P1, (450, 470))
        ecran.blit(self.texte_i8_p1_P2, (450, 510))
        ecran.blit(self.texte_i8_p1_P3, (450, 550))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i9_p1(self, ecran):
        self.texte_achat_rect.y = 650
        pygame.draw.rect(ecran, (255, 255, 255), [440, 515, 700, 180])
        ecran.blit(self.texte_i9_p1_P1, (450, 520))
        ecran.blit(self.texte_i9_p1_P2, (450, 560))
        ecran.blit(self.texte_i9_p1_P3, (450, 600))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i10_p1(self, ecran):
        self.texte_achat_rect.y = 660
        pygame.draw.rect(ecran, (255, 255, 255), [440, 565, 700, 130])
        ecran.blit(self.texte_i10_p1_P1, (450, 570))
        ecran.blit(self.texte_i10_p1_P2, (450, 610))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i1_p2(self, ecran):
        self.texte_achat_rect.y = 200
        pygame.draw.rect(ecran, (255, 255, 255), [440, 115, 700, 130])
        ecran.blit(self.texte_i1_p2_P1, (450, 120))
        ecran.blit(self.texte_i1_p2_P2, (450, 150))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i2_p2(self, ecran):
        self.texte_achat_rect.y = 220
        pygame.draw.rect(ecran, (255, 255, 255), [440, 165, 700, 80])
        ecran.blit(self.texte_i2_p2_P1, (450, 170))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i3_p2(self, ecran):
        self.texte_achat_rect.y = 300
        pygame.draw.rect(ecran, (255, 255, 255), [440, 215, 700, 130])
        ecran.blit(self.texte_i3_p2_P1, (450, 220))
        ecran.blit(self.texte_i3_p2_P2, (450, 250))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i4_p2(self, ecran):
        self.texte_achat_rect.y = 360
        pygame.draw.rect(ecran, (255, 255, 255), [440, 265, 700, 130])
        ecran.blit(self.texte_i4_p2_P1, (450, 270))
        ecran.blit(self.texte_i4_p2_P2, (450, 310))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i5_p2(self, ecran):
        self.texte_achat_rect.y = 410
        pygame.draw.rect(ecran, (255, 255, 255), [440, 315, 700, 130])
        ecran.blit(self.texte_i5_p2_P1, (450, 320))
        ecran.blit(self.texte_i5_p2_P2, (450, 360))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i6_p2(self, ecran):
        self.texte_achat_rect.y = 460
        pygame.draw.rect(ecran, (255, 255, 255), [440, 365, 700, 130])
        ecran.blit(self.texte_i6_p2_P1, (450, 370))
        ecran.blit(self.texte_i6_p2_P2, (450, 410))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i7_p2(self, ecran):
        self.texte_achat_rect.y = 510
        pygame.draw.rect(ecran, (255, 255, 255), [440, 415, 700, 130])
        ecran.blit(self.texte_i7_p2_P1, (450, 420))
        ecran.blit(self.texte_i7_p2_P2, (450, 460))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i8_p2(self, ecran):
        self.texte_achat_rect.y = 600
        pygame.draw.rect(ecran, (255, 255, 255), [440, 465, 700, 180])
        ecran.blit(self.texte_i8_p2_P1, (450, 470))
        ecran.blit(self.texte_i8_p2_P2, (450, 510))
        ecran.blit(self.texte_i8_p2_P3, (450, 550))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i9_p2(self, ecran):
        self.texte_achat_rect.y = 610
        pygame.draw.rect(ecran, (255, 255, 255), [440, 515, 700, 130])
        ecran.blit(self.texte_i9_p2_P1, (450, 520))
        ecran.blit(self.texte_i9_p2_P2, (450, 560))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i10_p2(self, ecran):
        self.texte_achat_rect.y = 660
        pygame.draw.rect(ecran, (255, 255, 255), [440, 565, 700, 130])
        ecran.blit(self.texte_i10_p2_P1, (450, 570))
        ecran.blit(self.texte_i10_p2_P2, (450, 610))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    #page 3
    def afichage_i1_p3(self, ecran):
        self.texte_achat_rect.y = 200
        pygame.draw.rect(ecran, (255, 255, 255), [440, 115, 700, 130])
        ecran.blit(self.texte_i1_p3_P1, (450, 120))
        ecran.blit(self.texte_i1_p3_P2, (450, 150))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i2_p3(self, ecran):
        self.texte_achat_rect.y = 260
        pygame.draw.rect(ecran, (255, 255, 255), [440, 165, 700, 130])
        ecran.blit(self.texte_i2_p3_P1, (450, 170))
        ecran.blit(self.texte_i2_p3_P2, (450, 210))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i3_p3(self, ecran):
        self.texte_achat_rect.y = 300
        pygame.draw.rect(ecran, (255, 255, 255), [440, 215, 700, 130])
        ecran.blit(self.texte_i3_p3_P1, (450, 220))
        ecran.blit(self.texte_i3_p3_P2, (450, 250))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i4_p3(self, ecran):
        self.texte_achat_rect.y = 360
        pygame.draw.rect(ecran, (255, 255, 255), [440, 265, 700, 130])
        ecran.blit(self.texte_i4_p3_P1, (450, 270))
        ecran.blit(self.texte_i4_p3_P2, (450, 310))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i5_p3(self, ecran):
        self.texte_achat_rect.y = 410
        pygame.draw.rect(ecran, (255, 255, 255), [440, 315, 700, 130])
        ecran.blit(self.texte_i5_p3_P1, (450, 320))
        ecran.blit(self.texte_i5_p3_P2, (450, 360))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
    def afichage_i6_p3(self, ecran):
        self.texte_achat_rect.y = 460
        pygame.draw.rect(ecran, (255, 255, 255), [440, 365, 700, 130])
        ecran.blit(self.texte_i6_p3_P1, (450, 370))
        ecran.blit(self.texte_i6_p3_P2, (450, 410))
        ecran.blit(self.texte_achat, self.texte_achat_rect)






    def afichage_i7_p3(self, ecran):
        self.texte_achat_rect.y = 510
        pygame.draw.rect(ecran, (255, 255, 255), [440, 415, 700, 130])
        ecran.blit(self.texte_i7_p2_P1, (450, 420))
        ecran.blit(self.texte_i7_p2_P2, (450, 460))
        ecran.blit(self.texte_achat, self.texte_achat_rect)

    def afichage_i8_p3(self, ecran):
        self.texte_achat_rect.y = 600
        pygame.draw.rect(ecran, (255, 255, 255), [440, 465, 700, 180])
        ecran.blit(self.texte_i8_p2_P1, (450, 470))
        ecran.blit(self.texte_i8_p2_P2, (450, 510))
        ecran.blit(self.texte_i8_p2_P3, (450, 550))
        ecran.blit(self.texte_achat, self.texte_achat_rect)

    def afichage_i9_p3(self, ecran):
        self.texte_achat_rect.y = 610
        pygame.draw.rect(ecran, (255, 255, 255), [440, 515, 700, 130])
        ecran.blit(self.texte_i9_p2_P1, (450, 520))
        ecran.blit(self.texte_i9_p2_P2, (450, 560))
        ecran.blit(self.texte_achat, self.texte_achat_rect)

    def afichage_i10_p3(self, ecran):
        self.texte_achat_rect.y = 660
        pygame.draw.rect(ecran, (255, 255, 255), [440, 565, 700, 130])
        ecran.blit(self.texte_i10_p2_P1, (450, 570))
        ecran.blit(self.texte_i10_p2_P2, (450, 610))
        ecran.blit(self.texte_achat, self.texte_achat_rect)
