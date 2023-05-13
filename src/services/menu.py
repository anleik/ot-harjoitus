from ui.button import Button
from entities.ground_object import GroundObject

button1_color = (70, 80, 160)
button2_color = (160, 40, 40)
bg_color = (80, 200, 80)



class MenuScreen:
    def __init__(self):
        self.button = Button()
        self.background_button = Button(0, 0, 800, 600, bg_color)
        self.level1_button = Button(125, 150, 200, 120, button1_color)
        self.level2_button = Button(475, 150, 200, 120, button2_color)
    def initialize_menu(self):
        Button.buttons.clear()
        Button.buttons.append(self.background_button)
        Button.buttons.append(self.level1_button)
        Button.buttons.append(self.level2_button)
        GroundObject.groundobjects.clear()
        GroundObject.groundobjects.append(GroundObject(0, 550, 1000, 40, bg_color))
