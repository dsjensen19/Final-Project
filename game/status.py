from arcade.arcade_types import Vector
from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
from game.gui_components.vector import Vector
from game.gui_components.objects.coin import Coin
from arcade import draw_rectangle_filled
from arcade import draw_rectangle_outline
from arcade import draw_text
from arcade import draw_circle_filled
from arcade import draw_circle_outline
from arcade import draw_polygon_filled
from arcade.color import(
    DARK_GRAY as gray,
    BLACK as black,
    RED as red,
    GREEN_YELLOW as green,
    GOLD as gold,
    BRONZE_YELLOW as brown,
    SILVER_SAND as silver
)
font_size = 12
width  = 200
height = 100
size = height / 12
x = screen_width - 100
y = screen_height - 50



compas_points = [[72,0],[57,15],[57,5],[57,5],[-30,5],[-45,15],[-70,15],[-55,0],[-70,-15],[-45,-15],[-30,-5],[57,-5],[57,-5],[57,-15]]
class Status_Indecator():

    def draw(self, centered_object):
        draw_rectangle_filled(x, y, width, height, gray)
        draw_rectangle_outline(x, y, width, height, gray)
        Coin()


        health_length = width * centered_object.curent_health/centered_object.get_max_health()
        draw_rectangle_filled(x, y + height/2 -  2*size, health_length, 2*size, red)
        supplies_length = width * centered_object.supplies/centered_object.get_hold()
        draw_rectangle_filled(x, y + height/2 -  6*size, supplies_length, 2*size, green)
        treasure_length = width * centered_object.treasure/centered_object.get_hold()
        draw_rectangle_filled(x, y + height/2 -  10*size, treasure_length, 2*size, gold)


        draw_rectangle_outline(x, y + height/2 -  2*size, width, 2*size, black)
        draw_rectangle_outline(x, y + height/2 -  6*size, width, 2*size, black) 
        draw_rectangle_outline(x, y + height/2 -  10*size, width, 2*size, black) 

        draw_text("Health", x - width/2, y + height/2 - 3*size, black, font_size, width, "center")
        draw_text("Supplies", x - width/2, y + height/2 - 7*size, black, font_size, width, "center")
        draw_text("Treasure", x - width/2, y + height/2 - 11*size, black, font_size, width, "center")
        draw_text(f"Gold {centered_object.get_gold()}", x - width/2, y + height/2 - 15*size, black, font_size, width, "center")


        to_haven = Vector(-centered_object.x + (screen_width / 2 + 100), -centered_object.y + screen_height / 2)
        angle = to_haven.angle
        x1 = screen_width - 100
        y1 = 100
        draw_circle_filled(x1, y1, 75, silver)
        draw_circle_outline(x1, y1, 75, black,2)
        

        new_points = []
        for point in compas_points:
            v = Vector(point[0],point[1])
            v.angle += angle
            new_points.append([v.dx+x1, v.dy+y1])        
        draw_polygon_filled(new_points,brown)