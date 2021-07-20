from game.fog_map import Fog_Map
import arcade
from game.game_engine import Game_Engine
from game.gui_components.objects.ship import Ship
from game.map import Map
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    REFRESH_RATE
)
def main(): 
    ship = Ship()
    map = Map()
    fog_map = Fog_Map()
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pirate")
    game_view = Game_Engine(ship, map, fog_map)
    window.show_view(game_view)
    window.set_update_rate(REFRESH_RATE)
    arcade.run()

if __name__ == "__main__":
    main()
