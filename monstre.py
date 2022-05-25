import pygame

class Monstre(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image/zombie.jpg')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.vitesse = 1
        self.vie = 100
        self.distance_joueur = 1000000

    def aller_manger_joueur(self,joueur):
        if joueur.rect.x > self.rect.x:
            self.rect.x += self.vitesse
        if joueur.rect.x < self.rect.x:
            self.rect.x -= self.vitesse
        if joueur.rect.y > self.rect.y:
            self.rect.y += self.vitesse
        if joueur.rect.y < self.rect.y:
            self.rect.y -= self.vitesse

    def bar_de_vie(self, ecran):
        pygame.draw.rect(ecran, (58, 58, 58), [self.rect.x - 30, self.rect.y - 10, 100, 5])
        pygame.draw.rect(ecran, (128, 5, 5), [self.rect.x - 30, self.rect.y - 10, self.vie, 5])
