import pygame

class Item:
    def __init__(self, y, texte, taille_police, prix):
        self.texte = texte
        self.prix = prix
        self.police = pygame.font.SysFont(pygame.font.get_fonts()[8], taille_police)
        self.image = self.police.render(texte, True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 255
        self.rect.y = y