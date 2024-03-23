# Battleships Conquer the Seas

Battleships: Command your fleet, unleash devastation, and conquer the seas in this epic game of naval warfare!

Battlships is a Python based terminal game which runs in the Code Institute mock terminal on Heroku. Users place their own ships on the board using the grid coordinates. Its then up to the user to find where the computers ships are before the computer finds theirs!

[Here is the live version of the site](https://battle-ships-conquer-the-seas-c0107b6ccc7a.herokuapp.com/)

![responsive-image](assets/images/responsive.png)

## How to play

Battleships is a classic game about naval warfare, sinking your opponents ships racing to hit all the opponents ships before they hit yours. You can read the full [wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) page for a better understanding.

In this version the player can insert their name and then choose the locations of their ships on a set grid. The ships are indicated by a X and then once all ships are placed they can begin against the computer.

The computer's ships are randomly generated and are hidden from the player to avoid cheating.

The player is given 15 turns to attmept to hit all 5 ships. If they dont manage to do this then the game ends. If they hit all 5 or the computer hits all 5 then the game also comes to and end congratulating the winner.

## Existing features

### Instructions:

- At the start of the game the instruction page gives all the information for the user to understand how to play and the layout of the game through the terminal

![instructions](assets/images/instructions.png)

### First Coordinate:

- The user is prompted to enter their name, after pressing enter the players board is generated where they are then asked for coordinates to place their ships onto the board.

![first_coordinate](assets/images/first_coordinate.png)

### Starting the game:

- Once all ships have been placed onto the board the game starts and both boards appear. prompting the user to take their first guess. 

![first_guess](assets/images/first_guess.png)

### Hitting a ship

- Once you hit a ship it will be marked on the board and you will recieve a "hit" string in the terminal.

![hit_ship](assets/images/hit_ship.png)

### Gameover

- After the moves are up the game will end.