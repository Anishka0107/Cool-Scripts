# Push into the Pit

A very simple naive Sokoban implementation & its AI based solver

### Steps to build
* Install `python3` and `pygame`
* To run the game : `python3 game.py`
* To run the solver : `python3 ai.py`
* To add more levels :
    * To add another level, add it as levels/levelX with X as the level number and update the program values accordingly
    * Make sure the board is of size 10 * 7 (drawback, will fix it some other day)
    * The program assumes that the level is valid (single player, num(boxes) <= num(pits)) and player's initial position is always on floor (never on pit)
    * Characters used for representation:
    	```
    	~ : Player
    	* : Box
    	+ : Pit
    	@ : Pit with Box in it
    	_ : Floor
    	# : Brick
    	```

Images taken from https://kenney.nl/assets/sokoban  
Logos taken from https://supalogo.com, https://cooltext.com 
