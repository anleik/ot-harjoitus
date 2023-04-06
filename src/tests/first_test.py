import pygame
import unittest
import os
from main import BackgroundObject


class TestBackgroundObject(unittest.TestCase):
    def setUp(self):
        self.bgo = BackgroundObject(1200, 260, 300, 100, 0.9, (135, 135, 255))

    def test_init(self):
        self.assertEqual(self.bgo.c, (135, 135, 255))
