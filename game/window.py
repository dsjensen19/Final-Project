import arcade
from arcade.color import BLACK, BLUE_GRAY as backround_color
import constants
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height,
    WORLD_DISTANCE
)
from game.gui_components.objects.ship import Ship
from game.gui_components.objects.backround import Backround
from game.map import Map
from game.gui_components.animations.move import Move
from game.gui_components.animations.turn import Turn

class Gui(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height)
        self.keys_held = []
        arcade.set_background_color(backround_color)
        self.set_update_rate(constants.REFRESH_RATE)

        """ your code here"""
        self.animations = []
        self.ship = Ship()
        self.backround = Backround()
        self.map = Map()

    def update(self, delta_time):
        self.while_key_held()
        """ your code here"""
        for ani in self.animations:
            if ani.is_finished:
                self.animations.remove(ani)
            else:
                ani.update()
        self.ship.update()
        self.map.update(self.ship)        

    def on_draw(self):
        arcade.start_render()
        """ your code here"""
        self.backround.draw()
        self.ship.draw()
        self.map.draw(self.ship)
    
    def on_key_press(self, key, key_modifiers):
        if not key in self.keys_held:
            self.keys_held.append(key)
        """ your code here"""   
        if key == arcade.key.KEY_1:
            self.ship.upgrade("speed")
        if key == arcade.key.KEY_2:
            self.ship.upgrade("vision")
        if key == arcade.key.KEY_3:
            self.ship.upgrade("hold")
        if key == arcade.key.KEY_4:
            self.ship.upgrade("crew")
        if key == arcade.key.KEY_5:
            self.ship.upgrade("health")

    def while_key_held(self):
        for key in self.keys_held:
            """ your code here"""
            if not self.ship.is_in_animation:
                self.animations.append(Turn(self.ship, key))
                self.animations.append(Move(self.ship, key))
        
    def on_key_release(self, key, key_modifiers):
        if key in self.keys_held:
            self.keys_held.remove(key)
        """ your code here"""

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ your code here"""
        pass
        
    def on_mouse_press(self, x, y, button, key_modifiers):
        """ your code here"""
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """ your code here"""
        pass
