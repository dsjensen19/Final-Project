import arcade
from arcade import draw_rectangle_filled
from arcade import draw_text
from arcade.color import BROWN
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
class Shop_Screen(arcade.View):
    def __init__(self, ship, game_view):
        self.ship = ship
        self.game_view = game_view
        super().__init__()
        self.speed_upgrade = rectangle(1,1,2,2)
        self.hold_upgrade = rectangle(1,1,2,2)
        self.health_upgrade = rectangle(1,1,2,2)
        self.vision_upgrade = rectangle(1,1,2,2)
        self.buy_supplies = rectangle(1,1,2,2)
        self.back_button = rectangle(250,250,300,300)

    def on_show(self):
        self.ship.in_port = False
        self.window.set_mouse_visible(True)
    def on_draw(self):
        arcade.start_render()
        self.speed_upgrade.draw()
        self.hold_upgrade.draw()
        self.health_upgrade.draw()
        self.vision_upgrade.draw()
        self.buy_supplies.draw()
        self.back_button.draw()
    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.speed_upgrade.on_click(x,y):
            self.ship.upgrade("speed")
        elif self.hold_upgrade.on_click(x,y):
            self.ship.upgrade("hold")
        elif self.health_upgrade.on_click(x,y):
            self.ship.upgrade("health")
        elif self.vision_upgrade.on_click(x,y):
            self.ship.upgrade("vision")
        elif self.buy_supplies.on_click(x,y):
            pass
        elif self.back_button.on_click(x,y):
            self.x = screen_width / 2
            self.y = screen_height / 2
            self.window.show_view(self.game_view)


class rectangle():
    def __init__(self, center_x, center_y, width, length ):
            self.center_x = center_x
            self.center_y = center_y
            self.width = width
            self.length = length
    def draw(self):
        draw_rectangle_filled(self.center_x, self.center_y, self.width, self.length, BROWN)
        pass

        
    def on_click(self, x, y,):
        """ Called when user lets off button """
        inside = True
        if x < (self.center_x - self.width/2):
            inside = False
        elif x > (self.center_x + self.width/2):
            inside = False
        elif y < (self.center_y - self.length/2):
            inside = False
        elif y > (self.center_y + self.length/2):
            inside = False
        return inside   