from .game_state import GameState
from .level1 import initialize_level1
from .level2 import initialize_level2
from .menu import MenuScreen



def level_select(gamestate: GameState):
    """Asettaa pelin haluttuun tasoon.

    Args:
        gamestate: Tämänhetkinen taso.
    """
    if gamestate.level != "":
        if gamestate.level == "level1":
            initialize_level1()
        elif gamestate.level == "level2":
            initialize_level2()
        elif gamestate.level == "menu":
            menu = MenuScreen()
            menu.initialize_menu()
    else:
        initialize_level1()
        gamestate.level = "level1"
