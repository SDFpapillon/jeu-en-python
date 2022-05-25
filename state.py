import pygame

class State(pygame.sprite.Sprite):

    def __init__(self):
        super.__init__()
        self.prodution_eau_auto = 0
        self.prodution_eau_max = 0
        self.demande_eau = 0