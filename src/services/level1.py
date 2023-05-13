from entities.goal import Goal
from entities.obstacle import Obstacle
from entities.ground_object import GroundObject
from entities.background_object import BackgroundObject
from entities.platform import Platform



ground_color = (140, 70, 20)
platform_color = (200, 70, 50)
obj_color = (135, 170, 235)
obj_color2 = (135, 135, 255)
obstacle_color = (0, 0, 0)

def initialize_level1():
    """Luo kaikki pelin oliot.
    """

    GroundObject.groundobjects.clear()
    GroundObject.groundobjects.append(GroundObject(10, 550, 1040, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(1240, 550, 840, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(2190, 550, 320, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(2700, 550, 320, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(3300, 550, 320, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(4000, 550, 320, 40, ground_color))
    GroundObject.groundobjects.append(GroundObject(4500, 550, 480, 40, ground_color))

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




    Platform.platforms.clear()
    Platform.platforms.append(Platform(400, 400, 100, 20, platform_color))
    Platform.platforms.append(Platform(600, 300, 150, 20, platform_color, 0.5))
    Platform.platforms.append(Platform(850, 200, 100, 20, platform_color))
    Platform.platforms.append(Platform(1160, 200, 100, 20, platform_color))
    Platform.platforms.append(Platform(3130, 530, 60, 20, platform_color))
    Platform.platforms.append(Platform(3600, 420, 80, 20, platform_color))
    Platform.platforms.append(Platform(3700, 300, 80, 20, platform_color))




    Obstacle.obstacles.clear()
    Obstacle.obstacles.append(Obstacle(400, 530, 60, 20))
    Obstacle.obstacles.append(Obstacle(790, 250, 40, 40))
    Obstacle.obstacles.append(Obstacle(970, 250, 180, 50))
    Obstacle.obstacles.append(Obstacle(1350, 450, 30, 100))
    Obstacle.obstacles.append(Obstacle(1820, 350, 180, 40))
    Obstacle.obstacles.append(Obstacle(2250, 350, 180, 40))
    Obstacle.obstacles.append(Obstacle(4620, 480, 50, 70))
    Obstacle.obstacles.append(Obstacle(4820, 450, 50, 100))


    Goal.goals.clear()
    Goal.goals.append(Goal(5130, 0, 100, 650))
