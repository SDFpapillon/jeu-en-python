import pygame
import time
import traceback
from jeu import Jeu
from ecrire_log import ecrire_log
from item import Item
pygame.init()


#génération fenetre
pygame.display.set_caption("nom du jeu")
ecran = pygame.display.set_mode((1080,700))

#import arrière plan
ArrierePlan = pygame.image.load('image/bg.jpg')

def sauvegarde():
    retour_ligne = "\n"

    ecrire_log.ecrire_log(self= ecrire_log, texte= " info : sauvegarde")


    sauvegarde = open('sauvegarde', 'w', 1)
    sauvegarde.write("true\n")

    sauvegarde.write("argent = \n")
    sauvegarde.write(str(jeu.joueur.argent))
    sauvegarde.write(retour_ligne)

    sauvegarde.write("nouriture = \n")
    sauvegarde.write(str(jeu.joueur.nouriture))
    sauvegarde.write(retour_ligne)

    sauvegarde.write("eau = \n")
    sauvegarde.write(str(jeu.joueur.eau))
    sauvegarde.write(retour_ligne)

    sauvegarde.write("batiment = \n")

    if jeu.atelier:
        sauvegarde.write("T\n")
    else:
        sauvegarde.write("F\n")

    if jeu.joueur.je_peux_mourir:
        sauvegarde.write("T\n")
    else:
        sauvegarde.write("F\n")

    if jeu.dessali1.rect.y > 0:
        sauvegarde.write("Dessali : T,")
        sauvegarde.write(str(jeu.dessali1.rect.x))
        sauvegarde.write(",")
        sauvegarde.write(str(jeu.dessali1.rect.y))
        sauvegarde.write(retour_ligne)
    else:
        sauvegarde.write("Dessali : F\n")

    if jeu.vache.rect.y > 0:
        sauvegarde.write("Vache : T,")
        sauvegarde.write(str(jeu.vache.rect.x))
        sauvegarde.write(",")
        sauvegarde.write(str(jeu.vache.rect.y))
        sauvegarde.write(retour_ligne)
    else:
        sauvegarde.write("Vache : F\n")

    if jeu.mais.rect.y > 0:
        sauvegarde.write("Mais : T,")
        sauvegarde.write(str(jeu.mais.rect.x))
        sauvegarde.write(",")
        sauvegarde.write(str(jeu.mais.rect.y))
        sauvegarde.write(retour_ligne)
    else:
        sauvegarde.write("Mais : F\n")

    if jeu.ble.rect.y > 0:
        sauvegarde.write("Blé : T,")
        sauvegarde.write(str(jeu.ble.rect.x))
        sauvegarde.write(",")
        sauvegarde.write(str(jeu.ble.rect.y))
        sauvegarde.write(retour_ligne)
    else:
        sauvegarde.write("Blé : F\n")

    if jeu.tourelle_1.rect.y > 0:
        sauvegarde.write("tourelle_1 : T,")
        sauvegarde.write(str(jeu.tourelle_1.rect.x))
        sauvegarde.write(",")
        sauvegarde.write(str(jeu.tourelle_1.rect.y))
        sauvegarde.write(retour_ligne)
    else:
        sauvegarde.write("tourelle_1 : F\n")

    if jeu.centrale_charbon.rect.y > 0:
        sauvegarde.write("centrale_charbon : T,")
        sauvegarde.write(str(jeu.centrale_charbon.rect.x))
        sauvegarde.write(",")
        sauvegarde.write(str(jeu.centrale_charbon.rect.y))
        sauvegarde.write(retour_ligne)
    else:
        sauvegarde.write("centrale_charbon : F\n")

    if jeu.mine.rect.y > 0:
        sauvegarde.write("mine : T,")
        sauvegarde.write(str(jeu.mine.rect.x))
        sauvegarde.write(",")
        sauvegarde.write(str(jeu.mine.rect.y))
        sauvegarde.write(retour_ligne)
    else:
        sauvegarde.write("mine : F\n")

    if jeu.mine.rect.y > 0:
        sauvegarde.write("mine_niveau_2 : T,")
        sauvegarde.write(str(jeu.mine_niveau_2.rect.x))
        sauvegarde.write(",")
        sauvegarde.write(str(jeu.mine_niveau_2.rect.y))
        sauvegarde.write(retour_ligne)
    else:
        sauvegarde.write("mine_niveau_2 : F\n")

    sauvegarde.write("Inventair = \n")
    for item in jeu.joueur.inventer:
        sauvegarde.write(jeu.joueur.inventer[item].texte)
        sauvegarde.write(",")
        sauvegarde.write(str(jeu.joueur.inventer[item].prix))
        sauvegarde.write(retour_ligne)

    sauvegarde.write("Boite = \n")
    for item in jeu.boite_de_stocage.items:
        sauvegarde.write(item.texte)
        sauvegarde.write(",")
        sauvegarde.write(str(item.prix))
        sauvegarde.write(retour_ligne)

    sauvegarde.close()

def verifier_variable():
    ecrire_log.ecrire_log(self= ecrire_log, texte=" info : recuperation des sauvegardes")

    sauvegarde = open('sauvegarde', 'r', 1)
    for i in range(3):
        ligne = sauvegarde.readline()
    jeu.joueur.argent = float(ligne)

    for i in range(2):
        ligne = sauvegarde.readline()
    jeu.joueur.nouriture = float(ligne)

    for i in range(2):
        ligne = sauvegarde.readline()
    jeu.joueur.eau = float(ligne)

    for i in range(2):
        ligne = sauvegarde.readline()

    if "T" in ligne:
        jeu.atelier = True
    ligne = sauvegarde.readline()

    if "T" in ligne:
        jeu.joueur.je_peux_mourir = True
    elif "F" in ligne:
        jeu.joueur.je_peux_mourir = False
    ligne = sauvegarde.readline()

    if "T" in ligne:
        co_x = ""
        co_y = ""
        partie = 0
        for lettre in ligne:
            if partie == 1:
                if lettre != ",":
                    co_x += lettre
            if partie == 2:
                if lettre != ",":
                    co_y += lettre
            if lettre == ",":
                partie += 1
        jeu.liste_batiment.append(Item(0, "dessalinisateur niveau 1........70", 30, 70))
        jeu.dessali1.rect.x = int(co_x)
        jeu.dessali1.rect.y = int(co_y)

    ligne = sauvegarde.readline()
    if "T" in ligne:
        co_x = ""
        co_y = ""
        partie = 0
        for lettre in ligne:
            if partie == 1:
                if lettre != ",":
                    co_x += lettre
            if partie == 2:
                if lettre != ",":
                    co_y += lettre
            if lettre == ",":
                partie += 1
        jeu.liste_batiment.append(Item(0, "vache.......180", 30, 180))
        jeu.vache.rect.x = int(co_x)
        jeu.vache.rect.y = int(co_y)

    ligne = sauvegarde.readline()
    if "T" in ligne:
        co_x = ""
        co_y = ""
        partie = 0
        for lettre in ligne:
            if partie == 1:
                if lettre != ",":
                    co_x += lettre
            if partie == 2:
                if lettre != ",":
                    co_y += lettre
            if lettre == ",":
                partie += 1
        jeu.liste_batiment.append(Item(0, "pousse de maïs......50", 30, 70))
        jeu.mais.rect.x = int(co_x)
        jeu.mais.rect.y = int(co_y)

    ligne = sauvegarde.readline()
    if "T" in ligne:
        co_x = ""
        co_y = ""
        partie = 0
        for lettre in ligne:
            if partie == 1:
                if lettre != ",":
                    co_x += lettre
            if partie == 2:
                if lettre != ",":
                    co_y += lettre
            if lettre == ",":
                partie += 1
        jeu.liste_batiment.append(Item(0, "pousse de blé......90", 30, 70))
        jeu.ble.rect.x = int(co_x)
        jeu.ble.rect.y = int(co_y)

    ligne = sauvegarde.readline()
    if "T" in ligne:
        co_x = ""
        co_y = ""
        partie = 0
        for lettre in ligne:
            if partie == 1:
                if lettre != ",":
                    co_x += lettre
            if partie == 2:
                if lettre != ",":
                    co_y += lettre
            if lettre == ",":
                partie += 1
        jeu.liste_batiment.append(Item(0, "tourelle de combat....450", 30, 450))
        jeu.tourelle_1.rect.x = int(co_x)
        jeu.tourelle_1.rect.y = int(co_y)

    ligne = sauvegarde.readline()
    if "T" in ligne:
        co_x = ""
        co_y = ""
        partie = 0
        for lettre in ligne:
            if partie == 1:
                if lettre != ",":
                    co_x += lettre
            if partie == 2:
                if lettre != ",":
                    co_y += lettre
            if lettre == ",":
                partie += 1
        jeu.liste_batiment.append(Item(0, "centrale au charbon.....6000", 30, 6000))
        jeu.centrale_charbon.rect.x = int(co_x)
        jeu.centrale_charbon.rect.y = int(co_y)

    ligne = sauvegarde.readline()
    if "T" in ligne:
        co_x = ""
        co_y = ""
        partie = 0
        for lettre in ligne:
            if partie == 1:
                if lettre != ",":
                    co_x += lettre
            if partie == 2:
                if lettre != ",":
                    co_y += lettre
            if lettre == ",":
                partie += 1
        jeu.liste_batiment.append(Item(0, "mine.......10000", 30, 10000))
        jeu.mine.rect.x = int(co_x)
        jeu.mine.rect.y = int(co_y)

    ligne = sauvegarde.readline()
    if "T" in ligne:
        co_x = ""
        co_y = ""
        partie = 0
        for lettre in ligne:
            if partie == 1:
                if lettre != ",":
                    co_x += lettre
            if partie == 2:
                if lettre != ",":
                    co_y += lettre
            if lettre == ",":
                partie += 1
        jeu.liste_batiment.append(Item(90, "mine niveau 2", 30, 0))
        jeu.mine_niveau_2.rect.x = int(co_x)
        jeu.mine_niveau_2.rect.y = int(co_y)

    ligne = sauvegarde.readline()
    for i in range(1,11):
        if "," in ligne:
            ligne = sauvegarde.readline()
            item = ""
            prix = ""

            partie = 1
            for lettre in ligne:
                if partie == 1:
                    if lettre != ",":
                        item += lettre
                if partie == 2:
                    if lettre != ",":
                        prix += lettre
                if lettre == ",":
                    partie += 1
            jeu.joueur.ajoute_inventer(item, int(prix))



    ligne = sauvegarde.readline()
    ligne = sauvegarde.readline()
    while "\n" in ligne:
        ligne = sauvegarde.readline()
        item = ""
        prix = ""

        partie = 1
        for lettre in ligne:
            if partie == 1:
                if lettre != ",":
                    item += lettre
            if partie == 2:
                if lettre != ",":
                    prix += lettre
            if lettre == ",":
                partie += 1
        jeu.boite_de_stocage.ajouter(item, prix)

#importé le jeu
jeu = Jeu(ecran)

jeu.boite_de_stocage.items.append(Item(0, "rien", 30, 0))

#boucle tant que EnMarche est vrai

texte = open('sauvegarde', 'r+', 1)
ligne_1 = texte.readlines()
if 'false\n' in ligne_1:
    texte.close()
if 'true\n' in ligne_1:
    verifier_variable()
    texte.close()

compteur = 0

while jeu.joueur.vivant:
    try :
        time.sleep(0.02)
        compteur += 1
        if compteur > 100:
            compteur = 0
            sauvegarde()


        #appliquer arrière plan
        ecran.blit(ArrierePlan, (0,-200))



        jeu.mise_A_jour(ecran)

        #mettre a jour l'écrant
        pygame.display.flip()

        # si il ferme la fenetre
        for event in pygame.event.get():
            # fermeture fenetre
            if event.type == pygame.QUIT:
                ecrire_log.ecrire_log(self= ecrire_log, texte=" info : quite le jeu")

                sauvegarde()
                jeu.joueur.vivant = False
                pygame.quit()
            # touche clavier
            elif event.type == pygame.KEYDOWN:
                jeu.presse[event.key] = True

            elif event.type == pygame.KEYUP:
                jeu.presse[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not jeu.attaque_en_cours:
                    if jeu.dessali1.rect.collidepoint(event.pos):
                        ecrire_log.ecrire_log(self= ecrire_log, texte=" info : dessalinisateur toucher")
                        jeu.afichage_info_batiment = True
                        jeu.info_batiment = jeu.dessali1
                    elif jeu.mais.rect.collidepoint(event.pos):
                        ecrire_log.ecrire_log(self= ecrire_log, texte=" info : maïs toucher")
                        jeu.afichage_info_batiment = True
                        jeu.info_batiment = jeu.mais
                    elif jeu.ble.rect.collidepoint(event.pos):
                        ecrire_log.ecrire_log(self= ecrire_log, texte=" info : blé toucher")
                        jeu.afichage_info_batiment = True
                        jeu.info_batiment = jeu.ble
                    elif jeu.vache.rect.collidepoint(event.pos):
                        ecrire_log.ecrire_log(self= ecrire_log, texte=" info : vache toucher")
                        jeu.afichage_info_batiment = True
                        jeu.info_batiment = jeu.vache
                    elif jeu.centrale_charbon.rect.collidepoint(event.pos):
                        ecrire_log.ecrire_log(self= ecrire_log, texte=" info : centrale au charbon toucher")
                        jeu.afichage_info_batiment = True
                        jeu.info_batiment = jeu.centrale_charbon
                    elif jeu.mine.rect.collidepoint(event.pos):
                        ecrire_log.ecrire_log(self= ecrire_log, texte=" info : mine toucher")
                        jeu.afichage_info_batiment = True
                        jeu.info_batiment = jeu.mine
                    elif jeu.mine_niveau_2.rect.collidepoint(event.pos):
                        ecrire_log.ecrire_log(self=ecrire_log, texte=" info : mine niveau 2 toucher")
                        jeu.afichage_info_batiment = True
                        jeu.info_batiment = jeu.mine_niveau_2

    except Exception as e:
        texte = " err : "
        texte += str(traceback.extract_tb(e.__traceback__, None))
        ecrire_log.ecrire_log(ecrire_log, texte)
        print(texte)
