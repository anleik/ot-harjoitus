import pygame
from .screen import screen

def draw_texts(distance, level):
    """Piirtää näytölle pelin tekstit:
    pelaajan liikkuma etäisyys,
    valikon ohjetekstit,
    tämänhetkinen taso,
    näppäinohjeet.

    Args:
        distance (float): Pelaajan liikkuma etäisyys tasossa.
        level    (str):   Tämänhetkinen taso.
    """

    font = pygame.font.SysFont("IMPACT", 34)
    text_color1 = (255, 255, 100)
    text_color2 = (20, 100, 20)
    text_color3 = (90, 50, 190)
    text_color4 = (0, 0, 0)
    if level != "menu":
        distance_text = font.render(f"{round(distance, 2)}", True, text_color1)
        m_text = font.render("m", True, text_color1)
        screen.blit(distance_text, (690, 10))
        screen.blit(m_text, (765, 10))
    else:
        level_select_text = font.render("SELECT LEVEL. CLICK BUTTONS WITH MOUSE.", True, text_color4)
        level1_text = font.render("Level 1: Easy", True, text_color4)
        level1_length = font.render("50 M", True, text_color4)
        level2_text = font.render("Level 2: Hard", True, text_color4)
        level2_length = font.render("100 M", True, text_color4)
        screen.blit(level_select_text, (120, 10))
        screen.blit(level1_text, (142, 170))
        screen.blit(level1_length, (190, 215))
        screen.blit(level2_text, (492, 170))
        screen.blit(level2_length, (540, 215))

    if level == "level1":
        level_text = font.render("Level 1: Easy", True, text_color2)
        screen.blit(level_text, (10, 10))

    if level == "level2":
        level_text = font.render("Level 2: Hard", True, text_color3)
        screen.blit(level_text, (10, 10))

    if distance < 10 or level == "menu":
        info_text = font.render("Arrow keys = MOVE. ESC = Save & Exit. R = Menu.", True, text_color4)
        screen.blit(info_text, (10, 550))
