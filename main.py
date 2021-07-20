from game.fog_map import Fog_Map
import arcade
from game.game_engine import Game_Engine
from game.gui_components.objects.ship import Ship
from game.map import Map
def main(): 
    ship = Ship()
    map = Map()
    fog_Map = Fog_Map()
    window = Game_Engine(ship, map, fog_Map)
    arcade.run()

if __name__ == "__main__":
    main()
