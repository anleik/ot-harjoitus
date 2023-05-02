import pygame
obstacle_color = (0, 0, 0)
class Obstacle:
    obstacles = []
    def __init__(self, obx = 0, oby = 0, obw = 0, obh = 0, color = obstacle_color):
        self.obx = obx
        self.oby = oby
        self.obw = obw
        self.obh = obh
        self.rect = pygame.Rect(obx, oby, obw, obh)
        self.color = color
