import pygame
from entities.background_object import BackgroundObject
from entities.ground_object import GroundObject
from entities.obstacle import Obstacle
from entities.platform import Platform
from entities.goal import Goal
from services.game_state import GameState
from services.level_select import level_select

from ui.text import draw_texts
from ui.screen import screen
from ui.game_ui import GameUI
from ui.button import Button


game_state = GameState()
level_select(game_state)


DEBUG = True

def main():
    """Gameloop, kutsuu inputin ja pelitapahtumien käsittelyn 
    sekä visuaalisten elementtien piirtämisen.
    """
    pygame.init()
    while game_state.running and DEBUG:
        # Input
        game_state.handle_events()
        game_state.update()

        # Draw + camera offset

        GameUI.fill(screen, game_state.level)
        GameUI.draw_bg_objects(BackgroundObject.backgroundobjects, game_state.background_offset)
        GameUI.draw_ground_objects(
            game_state.player, GroundObject.groundobjects, game_state.camera_offset)
        GameUI.draw_obstacles(game_state.player, Obstacle.obstacles, game_state.camera_offset)
        GameUI.draw_player(game_state.player, game_state.camera_offset)
        GameUI.draw_platforms(game_state.player, Platform.platforms, game_state.camera_offset)
        GameUI.draw_goals(Goal.goals, game_state.camera_offset)
        GameUI.draw_buttons(Button.buttons)

        draw_texts(game_state.distance, game_state.level)

        pygame.display.flip()

        game_state.clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
