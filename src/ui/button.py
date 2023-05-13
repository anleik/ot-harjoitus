import pygame
from .screen import screen
class Button:
    """Tasonvalintavalikon napit.
    """

    buttons = []
    def __init__(self, obj_x=0, obj_y=0, obj_w=0, obj_h=0, color=(255, 255, 255)):
        self.obx = obj_x
        self.oby = obj_y
        self.obw = obj_w
        self.obh = obj_h
        self.rect = pygame.Rect(obj_x, obj_y, obj_w, obj_h)
        self.color = color
