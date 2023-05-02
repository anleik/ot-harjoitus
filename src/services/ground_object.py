import pygame
ground_color = (140, 70, 20)
class GroundObject:
    """Maa, jonka päällä pelaaja voi seistä.
    """

    groundobjects = []
    def __init__(self, grx= 0, gry = 0, grw = 0, grh = 0, color = ground_color):
        self.grx = grx
        self.gry = gry
        self.grw = grw
        self.grh = grh
        self.rect = pygame.Rect(grx, gry, grw, grh)
        self.color = color
