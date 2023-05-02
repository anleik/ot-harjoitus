import pygame
from .screen import screen



class GameUI:

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

    def draw_player(Player, camera_offset):
        pygame.draw.rect(screen, Player.player_color, Player.player_rect.move(camera_offset, 0))

    def draw_platforms(Player, list, offset):
        for obj in list:
            if abs(Player.player_rect.x - obj.plx) < 1000:
                pygame.draw.rect(screen, obj.color, obj.rect.move(int(offset) ,0))
                if (Player.player_rect.x - obj.plx) > 1000:
                    list.remove(obj)

    def draw_goals(list, offset):
        for obj in list:
            pygame.draw.rect(screen, obj.color, obj.rect.move(offset, 0))

    
