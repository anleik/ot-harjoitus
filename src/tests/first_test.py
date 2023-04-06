import pygame
import unittest
import os
from main import BackgroundObject


class TestBackgroundObject(unittest.TestCase):
    def setUp(self):
        self.bgo = BackgroundObject(1200, 260, 300, 100, (135, 135, 255), 0.9)

    def test_init(self):
        self.assertEqual(self.bgo.color, (135, 135, 255))
