from constants import (
    SCREEN_WIDTH as screen_width,
    SCREEN_HEIGHT as screen_height)
from arcade import draw_rectangle_filled
from arcade import draw_rectangle_outline
from arcade import draw_text
from arcade.color import(
    DARK_GRAY as gray,
    BLACK as black,
    RED as red,
    GREEN_YELLOW as green,
    GOLD as gold
)
font_size = 12
width  = 200
height = 100
size = height / 12
x = screen_width - 100
y = screen_height - 50
class Status_Indecator():

    def draw(self, centered_object):
        draw_rectangle_filled(x, y, width, height, gray)
        draw_rectangle_outline(x, y, width, height, gray)


        health_length = width * centered_object.curent_health/centered_object.get_max_health()
        draw_rectangle_filled(x, y + height/2 -  2*size, health_length, 2*size, red)
        supplies_length = width * centered_object.supplies/centered_object.get_hold()
        draw_rectangle_filled(x, y + height/2 -  6*size, supplies_length, 2*size, green)
        tresure_length = width * centered_object.treasure/centered_object.get_hold()
        draw_rectangle_filled(x, y + height/2 -  10*size, tresure_length, 2*size, gold)

        draw_rectangle_outline(x, y + height/2 -  2*size, width, 2*size, black)
        draw_rectangle_outline(x, y + height/2 -  6*size, width, 2*size, black) 
        draw_rectangle_outline(x, y + height/2 -  10*size, width, 2*size, black) 


        draw_text("Health", x - width/2, y + height/2 - 3*size, black, font_size, width, "center")
        draw_text("Suplies", x - width/2, y + height/2 - 7*size, black, font_size, width, "center")
        draw_text("Tresure", x - width/2, y + height/2 - 11*size, black, font_size, width, "center")

0