import pygame
from.ground_object import GroundObject
from .background_object import BackgroundObject
from .platform import Platform
from .obstacle import Obstacle
from .goal import Goal
from .player import Player

ground_color = (140, 70, 20)
platform_color = (200, 70, 50)
obj_color = (135, 170, 235)
obj_color2 = (135, 135, 255)
obstacle_color = (0, 0, 0)

def initialize():
    GroundObject.groundobjects.clear()
    GroundObject.groundobjects.append(GroundObject(10, 550, 1050, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(2890, 550, 320, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(3450, 550, 100, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(3790, 550, 100, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(4130, 550, 100, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(4470, 550, 900, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(5600, 550, 300, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(6025, 550, 100, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(6250, 550, 100, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(6980, 550, 3020, 40, ground_color))

    BackgroundObject.backgroundobjects.clear()
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(1000, 260, 300, 100, obj_color2, 0.9))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(600, 40, 400, 200, obj_color, 0.3))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(1400, 150, 280, 150, obj_color2, 0.8))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(1500, 40, 400, 200, obj_color, 0.3))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(2500, 50, 300, 150, obj_color2, 0.8))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(3100, 100, 300, 100, obj_color2, 0.75))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(2500, 30, 300, 150, obj_color, 0.3))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(4000, 150, 300, 100, obj_color2, 0.8))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(5200, 120, 250, 80, obj_color2, 0.8))

    Platform.platforms.clear()
    Platform.platforms.append(Platform(400, 400, 100, 20, platform_color))
    Platform.platforms.append(Platform(600, 300, 150, 20, platform_color, 0.5))
    Platform.platforms.append(Platform(850, 200, 100, 20, platform_color))
    Platform.platforms.append(Platform(1240, 200, 100, 20, platform_color))
    Platform.platforms.append(Platform(1570, 200, 200, 20, platform_color))
    Platform.platforms.append(Platform(2020, 280, 180, 20, platform_color))
    Platform.platforms.append(Platform(2290, 420, 300, 20, platform_color))
    Platform.platforms.append(Platform(5190, 420, 80, 20, platform_color))
    Platform.platforms.append(Platform(4970, 280, 80, 20, platform_color))
    Platform.platforms.append(Platform(5190, 130, 80, 20, platform_color))
    Platform.platforms.append(Platform(5850, 160, 60, 20, platform_color))
    Platform.platforms.append(Platform(5990, 322, 70, 20, platform_color))
    Platform.platforms.append(Platform(6125, 97, 135, 20, platform_color))
    Platform.platforms.append(Platform(6160, 322, 70, 20, platform_color))
    Platform.platforms.append(Platform(6420, 400, 80, 20, platform_color))
    Platform.platforms.append(Platform(6500, 97, 100, 20, platform_color))

    Obstacle.obstacles.clear()
    Obstacle.obstacles.append(Obstacle(540, 360, 60, 150))
    Obstacle.obstacles.append(Obstacle(775, 250, 50, 50))
    Obstacle.obstacles.append(Obstacle(1000, 250, 100, 600))
    Obstacle.obstacles.append(Obstacle(1400, 100, 100, 100))
    Obstacle.obstacles.append(Obstacle(3035, 415, 30, 210))
    Obstacle.obstacles.append(Obstacle(4850, -100, 120, 550))
    Obstacle.obstacles.append(Obstacle(5270, 100, 120, 550))
    Obstacle.obstacles.append(Obstacle(5800, 0, 50, 395))
    Obstacle.obstacles.append(Obstacle(5850, 345, 400, 50))
    Obstacle.obstacles.append(Obstacle(6040, 120, 460, 50))
    Obstacle.obstacles.append(Obstacle(6500, 120, 100, 550))


    Goal.goals.clear()
    Goal.goals.append(Goal(10000+Player.player_rect.width, 0, 100, 650))

    Player.player_rect = pygame.Rect(100, 500, 30, 40)
    Player.DISTANCE = 0
    Player.PLAYER_VELOCITY_X = 0
    Player.BACKGROUND_OFFSET = 0
