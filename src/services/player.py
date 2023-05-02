import pygame

class Player:
    player_rect = pygame.Rect(100, 500, 30, 40)
    player_color = (255, 0, 0)
    DISTANCE = 0
    PLAYER_VELOCITY_X = 0
    PLAYER_VELOCITY_Y = 0
    BACKGROUND_OFFSET = 0
    JUMP_HEIGHT = 12
    ACCELERATION = 0.5
    DECELERATION = 0.8
    MAX_SPEED = 7.5

    @staticmethod
    def move(key=str):
        if key == "up":
            Player.PLAYER_VELOCITY_Y -= Player.JUMP_HEIGHT
