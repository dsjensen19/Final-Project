import arcade
from arcade.color import BLACK, BLUE_GRAY as backround_color
from random import randint as rand

import constants
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height
)
from game.gui_components.objects.ship import Ship
from game.gui_components.objects.backround import Backround
from game.gui_components.objects.island import Island
from game.gui_components.point import Point
from game.gui_components.animations.move import Move
from game.gui_components.animations.turn import Turn


class Gui(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height)
        self.keys_held = []
        arcade.set_background_color(backround_color)
        self.set_update_rate(constants.REFRESH_RATE)

        """ your code here"""
        self.objects = []
        self.animations = []

        self.ship = Ship()
        self.objects.append(Backround())

        self.objects.append(self.ship)
        for _ in range(500):
            self.create_island()

    def create_island(self):
        x = 100 * rand(-50, 50) + screen_width/2
        y = 100 * rand(-50, 50) + screen_height/2
        self.objects.append(Island(x = x, y = y))

    def update(self, delta_time):
        self.while_key_held()
        """ your code here"""
        for ani in self.animations:
            if ani.is_finished:
                self.animations.remove(ani)
            else:
                ani.update()
        for obj in self.objects:
                obj.update(self.ship)          

    def on_draw(self):
        arcade.start_render()
        """ your code here"""
        for obj in self.objects:
            if obj.is_on_screen:
                obj.draw(self.ship)
    
    def on_key_press(self, key, key_modifiers):
        if not key in self.keys_held:
            self.keys_held.append(key)
        """ your code here"""   

    def while_key_held(self):
        for key in self.keys_held:
            """ your code here"""
            if not self.ship.is_in_animation:
                self.animations.append(Turn(self.ship, .3, key))
                self.animations.append(Move(self.ship, .4, key))
        
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
