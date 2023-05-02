import pygame
from .screen import screen

def draw_texts(distance):
    font = pygame.font.SysFont("IMPACT", 34)
    text_color = (240, 240, 240)
    distance_text = font.render(f"{round(distance, 2)}", True, text_color)
    m_text = font.render("m", True, text_color)
    screen.blit(distance_text, (690, 10))
    screen.blit(m_text, (765, 10))
