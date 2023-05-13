import pygame
from entities.ground_object import GroundObject
from entities.platform import Platform
from entities.obstacle import Obstacle
from entities.goal import Goal
from database import sqlite
from ui.screen import SCREEN_WIDTH
from ui.button import Button
from .player import Player
from .level1 import initialize_level1
from .level2 import initialize_level2
from .menu import MenuScreen

MAX_JUMP_COUNTER = 15
class GameState:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.saved_progress = sqlite.progress_retrieve()
        self.distance = 0
        self.background_offset = 0
        self.camera_offset = 0
        self.is_jumping = False
        self.jump_counter = 0
        self.running = True
        self.gravity = 1.7
        self.level = ""
        self.menu = MenuScreen()
        self.keys = ""

        if self.saved_progress != []:
            self.player.player_rect.x = self.saved_progress[0][0]
            self.player.player_rect.y = self.saved_progress[0][1]
            self.level = self.saved_progress[0][2]
            self.background_offset -= self.player.player_rect.x

    def respawncheck(self, player):
        """Aloittaa tason alusta, jos pelaaja tippuu ulos näytöltä tai törmää esteeseen.
        """
        if player.player_rect.y > 900:
            self.respawn()
        if player.player_rect.collidelist(Obstacle.obstacles) >= 0:
            self.respawn()


    def respawn(self):
        self.player.player_rect = pygame.Rect(100, 500, 30, 40)
        self.distance = 0
        self.player.player_velocity_x = 0
        self.player.player_velocity_y = 0

    def goalcheck(self, player):
        """Tarkistaa onko pelaaja päässyt maaliin ja vaihtaa tason.

        Args:
            player: pelaaja
        """
        if self.level == "level1":
            if player.player_rect.collidelist(Goal.goals) >= 0:
                self.level = "level2"
                initialize_level2()
                self.respawn()
        if self.level == "level2":
            if player.player_rect.collidelist(Goal.goals) >= 0:
                self.level ="menu"
                self.menu.initialize_menu()
                self.respawn()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu.level1_button.rect.collidepoint(event.pos) and Button.buttons:
                    self.level = "level1"
                    Button.buttons.clear()
                    initialize_level1()
                    self.respawn()
                elif self.menu.level2_button.rect.collidepoint(event.pos) and Button.buttons:
                    self.level = "level2"
                    Button.buttons.clear()
                    initialize_level2()
                    self.respawn()
        self.key_press()

    def key_press(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_ESCAPE]:
            sqlite.save_progress(self.player.player_rect.x, self.player.player_rect.y, self.level)
            self.running = False
        if self.keys[pygame.K_UP] and not self.is_jumping:
            self.player.move("up")
            self.is_jumping = True
        if self.keys[pygame.K_LEFT]:
            self.player.move("left")
        elif self.keys[pygame.K_RIGHT]:
            self.player.move("right")
        elif self.keys[pygame.K_r]:
            self.level = "menu"
            self.menu.initialize_menu()
            self.respawn()
        else:
            self.player.player_velocity_x *= self.player.deceleration
            if abs(self.player.player_velocity_x) < 0.1:
                self.player.player_velocity_x = 0

    def collisions(self):
        """Tarkistaa koskettaako pelaaja maahan.
        """
        if self.player.player_rect.collidelist(GroundObject.groundobjects) >= 0:
            self.player.player_rect.y = int(
                GroundObject.groundobjects[self.player.player_rect.collidelist(
                    GroundObject.groundobjects)].gry - self.player.player_rect.height)
            self.is_jumping = False
            self.player.player_velocity_y = 0
            self.jump_counter = 0

        else:
            if self.keys[pygame.K_UP] and self.is_jumping and self.jump_counter < MAX_JUMP_COUNTER:
                self.player.player_velocity_y = -self.player.jump_height
                self.jump_counter += 1
            else:
                self.is_jumping = True
                self.jump_counter = MAX_JUMP_COUNTER

        for platform in Platform.platforms:
            if self.player.player_rect.colliderect(platform):
                if self.player.player_velocity_y > 0:
                    self.player.player_rect.y = platform.ply - self.player.player_rect.height
                    self.is_jumping = False
                    self.player.player_velocity_y, self.jump_counter = 0 , 0
                elif self.player.player_velocity_y < 0:
                    self.player.player_rect.y = platform.ply + platform.plh
                    self.player.player_velocity_y = 0

    def update(self):
        # Gravity and speed
        self.player.player_velocity_y += self.gravity
        self.player.player_rect.y += self.player.player_velocity_y
        self.player.player_rect.x += self.player.player_velocity_x

        self.collisions()

        # Background offset
        self.background_offset = -0.8 * self.player.player_rect.x
        self.distance = (self.player.player_rect.x - 100) / 100
        self.camera_offset = -self.player.player_rect.x + SCREEN_WIDTH // 2


        self.respawncheck(self.player)
        self.goalcheck(self.player)
