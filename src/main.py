import pygame
from database import sqlite
from services.ground_object import GroundObject
from services.background_object import BackgroundObject
from services.platform import Platform
from services.obstacle import Obstacle
from services.goal import Goal
from services.player import Player
from services.game_logic import *
from services.initialization import initialize

from ui.text import draw_texts
from ui.screen import screen, SCREEN_WIDTH # ,SCREEN_HEIGHT
from ui.game_ui import GameUI

pygame.init()

background_color = (135, 206, 235)

BACKGROUND_OFFSET = 0
PARALLAX_FACTOR = 0.5

# Camera scroll effect
camera_offset = -Player.player_rect.x + SCREEN_WIDTH // 2

initialize()

clock = pygame.time.Clock()

saved_progress = sqlite.progress_retrieve()
if saved_progress != []:
    Player.player_rect.x, Player.player_rect.y = saved_progress[0][0], saved_progress[0][1]
    BACKGROUND_OFFSET -= Player.player_rect.x

# Gameloop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sqlite.save_progress(Player.player_rect.x, Player.player_rect.y)
        RUNNING = False
    if keys[pygame.K_UP] and not IS_JUMPING:
        Player.move("up")
        IS_JUMPING = True
    if keys[pygame.K_LEFT]:
        Player.move("left")
    elif keys[pygame.K_RIGHT]:
        Player.move("right")
    else:
        Player.PLAYER_VELOCITY_X *= Player.DECELERATION
        if abs(Player.PLAYER_VELOCITY_X) < 0.1:
            Player.PLAYER_VELOCITY_X = 0


    # Gravity and speed
    Player.PLAYER_VELOCITY_Y += GRAVITY
    Player.player_rect.y += Player.PLAYER_VELOCITY_Y
    Player.player_rect.x += Player.PLAYER_VELOCITY_X

    # Ground Collisions
    if Player.player_rect.collidelist(GroundObject.groundobjects) >= 0:
        Player.player_rect.y = int(
            GroundObject.groundobjects[Player.player_rect.collidelist(
                GroundObject.groundobjects)].gry - Player.player_rect.height)
        IS_JUMPING = False
        Player.PLAYER_VELOCITY_Y = 0
        JUMP_COUNTER = 0
    else:
        # High jump
        if keys[pygame.K_UP] and IS_JUMPING and JUMP_COUNTER < MAX_JUMP_COUNTER:
            Player.PLAYER_VELOCITY_Y = -Player.JUMP_HEIGHT
            JUMP_COUNTER += 1
        else:
            IS_JUMPING = True
            JUMP_COUNTER = MAX_JUMP_COUNTER

    # Platform Collisions
    for platform in Platform.platforms:
        if Player.player_rect.colliderect(platform):
            if Player.PLAYER_VELOCITY_Y > 0:  # Above collision
                Player.player_rect.y = platform.ply - Player.player_rect.height
                IS_JUMPING = False
                Player.PLAYER_VELOCITY_Y = 0
                JUMP_COUNTER = 0
            elif Player.PLAYER_VELOCITY_Y < 0:  # Below collision
                Player.player_rect.y = platform.ply + platform.plh
                Player.PLAYER_VELOCITY_Y = 0

    # Background offset
    BACKGROUND_OFFSET = -0.8 * Player.player_rect.x
    DISTANCE = (Player.player_rect.x - 100) / 100
    camera_offset = -Player.player_rect.x + SCREEN_WIDTH // 2

    # Respawn
    respawncheck()

    # Draw + camera offset
    screen.fill(background_color)
    GameUI.draw_bg_objects(BackgroundObject.backgroundobjects, BACKGROUND_OFFSET)
    GameUI.draw_ground_objects(Player, GroundObject.groundobjects, camera_offset)
    GameUI.draw_obstacles(Player, Obstacle.obstacles, camera_offset)
    GameUI.draw_player(Player, camera_offset)
    GameUI.draw_platforms(Player, Platform.platforms, camera_offset)
    GameUI.draw_goals(Goal.goals, camera_offset)

    draw_texts(DISTANCE)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
