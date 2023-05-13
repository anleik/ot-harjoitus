import pygame

class Player:
    """Pelaajahahmon ominaisuuksia.
    """
    def __init__(self):
        self.player_rect = pygame.Rect(100, 500, 30, 40)
        self.player_color = (255, 0, 0)
        self.player_velocity_x = 0
        self.player_velocity_y = 0
        self.jump_height = 12
        self.acceleration = 0.5
        self.deceleration = 0.8
        self.max_speed = 7.5



    def move(self, key:str):
        """Liikuttaa pelaajaa halutun näppäimen mukaan.

        Args:
            key (str): Painettu näppäin.  
        """

        if key == "up":
            self.player_velocity_y -= self.jump_height
        if key == "left":
            self.player_velocity_x -= self.acceleration
            self.player_velocity_x = max(self.player_velocity_x, -self.max_speed)
        if key == "right":
            self.player_velocity_x += self.acceleration
            self.player_velocity_x = min(self.player_velocity_x, self.max_speed)
