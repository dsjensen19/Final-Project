from game.gui_components.objects.game_object import Game_Object
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)

class Ship(Game_Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        speed_values = [1, 2, 3, 4, 5]
        vision_values = [3, 4, 5, 6, 7]
        hold_values = [200, 350, 500, 700, 1000]
        crew_values = [5, 7, 9, 12, 16]

        speed_level = 0
        vision_level = 0
        hold_level = 0
        crew_level = 0

        self.current_speed = speed_values[0]
        self.current_vision = vision_values[0]
        self.current_hold = hold_values[0]
        self.current_crew = crew_values[0]

     def upgrade(self, trait):

        if (trait == speed):
          speed_level += 1
          self.current_speed = speed_values[speed_level]
        elif (trait == vision):
          vision_level += 1
          self.current_vision = vision_values[vision_level]
        elif (trait == hold):
          hold_level += 1
          self.current_hold = hold_values[hold_level]
        elif (trait == crew):
          crew_level += 1
          self.current_crew = crew_values[crew_level]


    def get_speed(self):
        return self.current_speed

    def get_vision(self):
        return self.current_vision

    def get_hold(self):
        return self.current_hold

    def get_crew(self):
        return self.current_crew

    def draw(self):
        x = screen_width / 2
        y = screen_height / 2
        self.sprite.draw(x, y)
