# Final-Project

Okeydoke,So here's the way that the game is played. Conecpts first, then we make the final framework

So there is the pirate haven, an island where you start the game
in all directions, there is fog. The ocean is made up of various tiles
when you travel, you see through a certain number os squares of fog. These squares remain unfoggy
You find islands (several tiles large). when you sail to each square of the island, you loot that part
of the island for stuff (either just straight gold or various valuable things that can be sold for gold at pirate haven)
Every square you move costs supplies. You have a limited cargo hold for holding supplies and loot

you can upgrade cargo, crew, sight, cannons

end of game is falling off of the edge of the world

storm refills islands and resets fog


the map is a dictionary. The Key is the name and the value are x and y coordinates

______________________________________________________

              CLASSES AND ASSINGMENTS
______________________________________________________
AUTHOR NAMES: Tyson Brost, Derek Jensen, Seth Burton, Chris Patrinovich


Ship (Game Object) : Moves across screen carries values for the current health, supplies, crew and sight/cannon levels
    Assigned to - 
Constants : sets screen size, movement rates, island count, storm/loot frequency
    Assigned to - 
Director :
    Assigned to - 
Buffer :Hold and display dynamic user input
    Assigned to - 
InputService : takes user input
    Assigned to - 
OutputSerivce : updates game board
    Assigned to - 
Score : tracks player score (Gold)
    Assigned to - 
Player : gives input 
    Assigned to - 
Map : generated to a set size, contains numerous islands and a pirate haven.
    Assigned to - 
Cargo hold (Game Object):
    Assigned to -
Island (Game Object) : Randomly generated shapes/sizes and locations
    Assigned to - 
Storm : occurs at random movement intervals? (every 100-200 moves?), resets islands and loot
    Assigned to - 

