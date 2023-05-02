#import pygame
from .player import Player
from .obstacle import Obstacle
from .initialization import initialize

PLAYER_SPEED = 5
GRAVITY = 1.70

IS_JUMPING = False

KEY_UP_PRESSED = False
JUMP_KEY_TIME = 0
MAX_JUMP_TIME = 0.5
JUMP_COUNTER = 0
MAX_JUMP_COUNTER = 15


def respawncheck():
    """Aloittaa tason alusta, jos pelaaja tippuu ulos näytöltä tai törmää esteeseen.
    """

    if Player.player_rect.y > 900:
        initialize()
    if Player.player_rect.collidelist(Obstacle.obstacles) >= 0:
        initialize()
