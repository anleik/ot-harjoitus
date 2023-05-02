import pygame

class Player:
    """Pelaajahahmon ominaisuuksia.
    """

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
        """Liikuttaa pelaajaa halutun näppäimen mukaan.

        Args:
            key (str): Painettu näppäin jota voisi simuloida testissä jos osaisin.  
        """

        if key == "up":
            Player.PLAYER_VELOCITY_Y -= Player.JUMP_HEIGHT
        if key == "left":
            Player.PLAYER_VELOCITY_X -= Player.ACCELERATION
            Player.PLAYER_VELOCITY_X = max(Player.PLAYER_VELOCITY_X, -Player.MAX_SPEED)
        if key == "right":
            Player.PLAYER_VELOCITY_X += Player.ACCELERATION
            Player.PLAYER_VELOCITY_X = min(Player.PLAYER_VELOCITY_X, Player.MAX_SPEED)
