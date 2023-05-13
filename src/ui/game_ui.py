import pygame
from .screen import screen



class GameUI:
    """Piirtää pelin objektit.

    Args:
        list: lista jossa säilytetään kaikki kyseiset oliot.
        Player: Pelaajaluokka jota on vain 1.
        offset: arvo, joka varmistaa että oliot liikkuvat samaan tahtiin kuin pelaaja.
    """

    def draw_bg_objects(list, offset):
        for obj in list:
            pygame.draw.rect(screen, obj.color, obj.rect.move(
                (int(offset * obj.par)), 0))

    def draw_ground_objects(Player, list, offset):
        for obj in list:
            if abs(Player.player_rect.x - obj.grx) < 3000:
                pygame.draw.rect(screen, obj.color, obj.rect.move(offset, 0))



    def draw_obstacles(Player, list, offset):
        for obj in list:
            if abs(Player.player_rect.x - obj.obx) < 2000:
                pygame.draw.rect(screen, obj.color, obj.rect.move(offset, 0))
                if (Player.player_rect.x - obj.obx) > 2000:
                    list.remove(obj)

    def draw_player(Player, offset):
        pygame.draw.rect(screen, Player.player_color, Player.player_rect.move(offset, 0))

    def draw_platforms(Player, list, offset):
        for obj in list:
            if abs(Player.player_rect.x - obj.plx) < 1000:
                pygame.draw.rect(screen, obj.color, obj.rect.move(int(offset) ,0))
                if (Player.player_rect.x - obj.plx) > 1000:
                    list.remove(obj)

    def draw_goals(list, offset):
        for obj in list:
            pygame.draw.rect(screen, obj.color, obj.rect.move(offset, 0))

    def draw_buttons(list):
        for obj in list:
            pygame.draw.rect(screen, obj.color, obj.rect)

    def fill(screen, level):
        if level == "level1":
            color = (135, 206, 235)
        elif level =="level2":
            color = (120, 20, 20)
        else:
            color = (120, 240, 120)
        screen.fill(color)
