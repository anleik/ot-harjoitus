import pygame
goal_color = (0, 200, 0)
class Goal:
    """Maali, johon pelaajan tavoite on päästä.
    """

    goals = []
    def __init__(self, goalx = 0, goaly = 0, goalw = 0, goalh = 0, color = goal_color):
        self.goalx = goalx
        self.goaly = goaly
        self.goalw = goalw
        self.goalh = goalh
        self.rect = pygame.Rect(goalx, goaly, goalw, goalh)
        self.color = color
