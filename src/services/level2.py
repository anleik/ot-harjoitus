from entities.obstacle import Obstacle
from entities.background_object import BackgroundObject
from entities.platform import Platform
from entities.goal import Goal
from entities.ground_object import GroundObject

ground_color = (80, 30, 10)
platform_color = (160, 70, 0)
obj_color = (100, 30, 30)
obj_color2 = (150, 40, 60)
obstacle_color = (0, 0, 0)

def initialize_level2():
    """Luo kaikki pelin oliot.
    """

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
        BackgroundObject(1000, 460, 300, 200, obj_color, 0.9))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(600, 370, 400, 300, obj_color, 0.3))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(1400, 450, 280, 200, obj_color2, 0.8))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(1500, 420, 400, 200, obj_color, 0.3))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(2500, 380, 300, 250, obj_color2, 0.8))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(3100, 400, 300, 200, obj_color2, 0.75))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(2500, 430, 300, 190, obj_color, 0.3))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(4000, 350, 300, 300, obj_color2, 0.8))
    BackgroundObject.backgroundobjects.append(
        BackgroundObject(5200, 420, 250, 190, obj_color2, 0.8))

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
    Platform.platforms.append(Platform(8975, 480, 350, 20, platform_color))
    Platform.platforms.append(Platform(9475, 300, 350, 20, platform_color))

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
    Obstacle.obstacles.append(Obstacle(7800, 500, 40, 50))
    Obstacle.obstacles.append(Obstacle(7800, 0, 40, 370))
    Obstacle.obstacles.append(Obstacle(8000, 475, 40, 75))
    Obstacle.obstacles.append(Obstacle(8000, 0, 40, 345))
    Obstacle.obstacles.append(Obstacle(8200, 450, 40, 100))
    Obstacle.obstacles.append(Obstacle(8200, 0, 40, 320))
    Obstacle.obstacles.append(Obstacle(8400, 425, 40, 125))
    Obstacle.obstacles.append(Obstacle(8400, 0, 40, 295))
    Obstacle.obstacles.append(Obstacle(8600, 400, 40, 150))
    Obstacle.obstacles.append(Obstacle(8600, 0, 40, 260))
    Obstacle.obstacles.append(Obstacle(9000, 0, 300, 420))
    Obstacle.obstacles.append(Obstacle(9000, 500, 300, 120))
    Obstacle.obstacles.append(Obstacle(9500, 0, 300, 240))
    Obstacle.obstacles.append(Obstacle(9500, 320, 300, 280))


    Goal.goals.clear()
    Goal.goals.append(Goal(10030, 0, 100, 650))
