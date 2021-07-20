import arcade
from arcade import draw_rectangle_filled
from arcade import draw_scaled_texture_rectangle
from arcade import load_texture
from arcade import draw_text
from arcade import draw_rectangle_outline
from arcade.color import BLACK, WHITE
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
from arcade.color import(
    DARK_GRAY as gray,
    BLACK as black,
    RED as red,
    GREEN_YELLOW as green,
    GOLD as gold,
    BRONZE_YELLOW as brown,
    SILVER_SAND as silver)


class Shop_Screen(arcade.View):
    def __init__(self, ship, game_view):
        self.ship = ship
        self.game_view = game_view
        super().__init__()
        self.speed_upgrade = rectangle(1100,650,150,100, "Upgrade Sails")
        self.hold_upgrade = rectangle(875,650,150,100, "Upgrade cargo hold")
        self.health_upgrade = rectangle(650,650,150,100, "Upgrade Hull")
        self.vision_upgrade = rectangle(425,650,150,100, "Upgrade Crows Nest")
        self.buy_supplies = rectangle(200,650,150,100, "Buy Supplies")
        self.back_button = rectangle(screen_width/2, screen_height /2,150,100, "Set Sail")
        self.backround_t = load_texture("sprite_images\cove.png")
        self.scale1 = 1
        

        

    def on_show(self):
        self.ship.in_port = False
        self.window.set_mouse_visible(True)
        
    def on_draw(self):
        arcade.start_render()
        draw_scaled_texture_rectangle(screen_width/2, screen_height /2, self.backround_t, self.scale1, 0)
        self.speed_upgrade.draw()
        self.hold_upgrade.draw()
        self.health_upgrade.draw()
        self.vision_upgrade.draw()
        self.buy_supplies.draw()
        self.back_button.draw()


        font_size = 12
        width  = 200
        height = 100
        size = height / 12
        x = screen_width - 100
        y = screen_height - 300
        draw_rectangle_filled(x, y, width, height, gray)
        draw_rectangle_outline(x, y, width, height, gray)
        
        texture = load_texture("sprite_images\coin.png")
        scale = 1
        draw_scaled_texture_rectangle((screen_width - 100), (y + height/2 -  14*size), texture, scale, 0)
        scale = .6

        supplies_length = width * self.ship.supplies/self.ship.get_hold()
        draw_rectangle_filled(x, y + height/2 -  6*size, supplies_length, 2*size, green)
        draw_rectangle_outline(x, y + height/2 -  6*size, width, 2*size, black) 
         
        draw_text("Supplies", x - width/2, y + height/2 - 7*size, black, font_size, width, "center")
        draw_text(f"{self.ship.get_gold()}", x - width/2, y + height/2 - 15*size, black, font_size + 2, width, "center")
    
    
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
            self.ship.upgrade("supplies")
        elif self.back_button.on_click(x,y):
            self.x = (screen_width / 2) + 100
            self.y = (screen_height / 2) + 300
            self.window.show_view(self.game_view)


class rectangle():
    def __init__(self, center_x, center_y, width, length, text):
            self.center_x = center_x
            self.center_y = center_y
            self.width = width
            self.length = length
            self.font_size = 16
            self.text = text
    def draw(self):
        texture = load_texture("sprite_images\wood.png")
        scale = .3
        draw_scaled_texture_rectangle(self.center_x, self.center_y, texture, scale, 0)
        draw_text(self.text, self.center_x - self.width/2, self.center_y-25, WHITE, self.font_size, self.width, "center")
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