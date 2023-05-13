import pygame
import unittest
from unittest.mock import patch, MagicMock
import os
import main
from services.game_state import GameState
from services.level2 import initialize_level2

class TestBackgroundObject(unittest.TestCase):
    def setUp(self):
        DEBUG = False
        self.bgo = main.BackgroundObject(1200, 260, 300, 100, (135, 135, 255), 0.9)

    def test_init(self):
        self.assertEqual(self.bgo.color, (135, 135, 255))

class TestGameState(unittest.TestCase):
    def setUp(self):
        main.DEBUG = False
        initialize_level2()
        self.g = GameState()

    def test_handle_events(self):
        main.DEBUG = False
        pygame.quit()
        self.assertEqual(self.g.running, True)



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
