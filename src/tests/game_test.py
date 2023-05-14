import pygame
import unittest
from unittest.mock import patch, MagicMock
import os
import main
from database import sqlite
from services.game_state import GameState
from services.level2 import initialize_level2
from services import level_select
from entities import ground_object
from entities import obstacle
from entities import goal
from ui import button

class TestGameState(unittest.TestCase):
    def setUp(self):
        main.DEBUG = False
        self.g = GameState()
        self.g.level = "nonsense"
        level_select.level_select(self.g)

    def test_running(self):
        main.DEBUG = False
        pygame.quit()
        self.assertEqual(self.g.running, True)

    def test_level_1(self):
        initial_value = len(ground_object.GroundObject.groundobjects)
        self.g.level = ""
        level_select.level_select(self.g)
        self.g.level = "level1"
        level_select.level_select(self.g)
        self.assertNotEqual(initial_value, len(ground_object.GroundObject.groundobjects))

    def test_level_2(self):
        initial_value = len(ground_object.GroundObject.groundobjects)
        self.g.level = "level2"
        level_select.level_select(self.g)
        self.assertNotEqual(initial_value, len(ground_object.GroundObject.groundobjects))

    def test_level_menu(self):
        self.g.level = "level1"
        level_select.level_select(self.g)
        initial_value = len(ground_object.GroundObject.groundobjects)
        self.g.level = "menu"
        level_select.level_select(self.g)
        self.assertNotEqual(initial_value, len(ground_object.GroundObject.groundobjects))

    def test_save_progress(self):
        self.g.level = "level1"
        self.g.player.player_rect.x = 200
        initx, inity, initlevel = self.g.player.player_rect.x, self.g.player.player_rect.y, self.g.level
        sqlite.save_progress(initx, inity, initlevel)
        self.gg  = GameState()
        self.assertEqual((initx, inity, initlevel), (self.gg.player.player_rect.x, self.gg.player.player_rect.y, self.gg.level))

    def test_player_out_of_bounds(self):
        self.g.player.player_rect.y = 1000
        self.g.respawncheck(self.g.player)
        self.assertNotEqual(1000, self.g.player.player_rect.y)
    
    def test_obstacle_collision(self):
        self.g.player.player_rect.x, self.g.player.player_rect.y = 300, 300
        obstacle.Obstacle.obstacles.append(obstacle.Obstacle(290, 290, 50, 50))
        self.g.respawncheck(self.g.player)
        self.assertNotEqual(self.g.player.player_rect.x, 300)

    def test_goal_check_level_1(self):
        self.g.level = "level1"
        self.g.player.player_rect.x, self.g.player.player_rect.y = 300, 300
        goal.Goal.goals.append(goal.Goal(290, 290, 50, 50))
        self.g.goalcheck(self.g.player)
        self.assertEqual("level2", self.g.level)
        self.assertNotEqual(300, self.g.player.player_rect.x)

    def test_goal_check_level_2(self):
        self.g.level = "level2"
        self.g.player.player_rect.x, self.g.player.player_rect.y = 500, 500
        goal.Goal.goals.append(goal.Goal(450, 400, 51, 101))
        self.g.goalcheck(self.g.player)
        self.assertEqual("menu", self.g.level)
        self.assertNotEqual(500, self.g.player.player_rect.x)



class TestPlayerMove(unittest.TestCase):
    def setUp(self):
        self.game_state = GameState()
        self.player = self.game_state.player


    def test_player_jump(self):
        initial_velocity_y = self.player.player_velocity_y
        self.player.move("up")
        self.assertNotEqual(self.player.player_velocity_y, initial_velocity_y)


    def test_player_move_left(self):
        initial_velocity_x = self.player.player_velocity_x
        self.player.move("left")
        self.assertNotEqual(self.player.player_velocity_x, initial_velocity_x)
    
    def test_player_move_right(self):
        initial_velocity_x = self.player.player_velocity_x
        self.player.move("right")
        self.assertNotEqual(self.player.player_velocity_x, initial_velocity_x)
