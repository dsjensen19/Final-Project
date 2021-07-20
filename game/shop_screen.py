import arcade
from arcade import draw_rectangle_filled
from arcade import draw_text
class Shop_Screen(arcade.View):
    def __init__(self, ship, game_view):
        self.ship = ship
        self.game_view = game_view
        super().__init__()
        self.speed_upgrade = rectangle(1,1,1,1)
        self.hold_upgrade = rectangle(1,1,1,1)
        self.health_upgrade = rectangle(1,1,1,1)
        self.vision_upgrade = rectangle(1,1,1,1)
        self.buy_supplies = rectangle(1,1,1,1)
        self.back_button = rectangle(1,1,1,1)

    def on_show(self):
        self.set_mouse_visible = True
        self.ship.in_port = False

    def on_draw(self):
        arcade.start_render()
        self.speed_upgrade.draw()
        self.hold_upgrade.draw()
        self.health_upgrade.draw()
        self.vision_upgrade.draw()
        self.buy_supplies.draw()
        self.back_button.draw()
    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.speed_upgrade():
            self.ship.upgrade("speed")
        elif self.hold_upgrade():
            self.ship.upgrade("hold")
        elif self.health_upgrade():
            self.ship.upgrade("health")
        elif self.vision_upgrade():
            self.ship.upgrade("vision")
        elif self.buy_supplies():
            pass
        elif self.back_button():
            self.window.show_view(self.game_view)


class rectangle():
    def __init__(self, center_x, center_y, width, length ):
            self.center_x=center_x,
            self.center_y=center_y,
            self.width = width,
            self.length= length
    def draw(self):
        #  draw_rectangle_filled(self.center_x, self.center_y, self.width, self.length, arcade.color.BROWN)
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