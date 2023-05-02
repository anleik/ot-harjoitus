import pygame
platform_color = (200, 70, 50)
class Platform:
    platforms = []
    def __init__(self, plx= 0, ply = 0, plw = 0, plh = 0, color = platform_color, par = 1):
        self.plx = plx
        self.ply = ply
        self.plw = plw
        self.plh = plh
        self.rect = pygame.Rect(plx, ply, plw, plh)
        self.color = color
        self.par = par
