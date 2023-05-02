import pygame
class BackgroundObject:
    backgroundobjects = []
    def __init__(self, obj_x=0, obj_y=0, obj_w=0, obj_h=0, color=(255, 255, 255), par = 1):
        self.rect = pygame.Rect(obj_x, obj_y, obj_w, obj_h)
        self.color = color
        self.par = par
