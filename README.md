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

## User Experience

#### Visitors to this website are looking for:

- A simple game of battleships, not overcomplicated whilst remaining visually pleasing. The clear instructions at the start create a fair experience as every user is given access to the full rule set before they start playing regardless if they have played before. This was decided due to a few people who I spoke to regarding testing the game who didn't know exactly how to play.

#### Creating a clear board style

- When designing the game I opted for the use of an external border made of "~" to make it easier for the user to see the board boundaries and to avoid any empty space that some users can cause discomfort or confusion. I tested a few different symbols/characters to see what worked best and eventually decided on the "~" due to the clear separation it made whilst looking appealing in the terminal.

## Existing features

### Instructions:

- At the start of the game the instruction page gives all the information for the user to understand how to play and the layout of the game through the terminal. As seen below the title is separated from the objective and the same for the instructions. This helps with readablity as its not all squashed into one single paragraph. At the bottom it then gives the option for the player to enter their name to begin playing.

![instructions](assets/images/instructions.png)

### First Coordinate:

- The user is prompted to enter their name, after pressing enter the players, and computers boards are generated. The user is then asked for coordinates to place their ships onto the board. This decision was made to allow the user full control over their ship placement giving them the feeling that they have control, if it was random then it could give the feeling that it's biased towards the computer.

![first_coordinate](assets/images/first_coordinate.png)

### Starting the game:

- Once all ships have been placed onto the board the game starts and both boards appear. Prompting the user to take their first guess. They also have a clear "Moves left" at the top of the board, informing the player that they need to be careful with their guesses as they are limited.

![first_guess](assets/images/first_guess.png)

### Hitting or missing a ship

- Once you hit a ship it will be marked on the board and you will recieve a "hit" string in the terminal.
- For missing a ship you will receieve a "-" on the board which will show you the coordinates you chose. That mark will then remain on there for the rest of the game so you don't choose them again. If the player does decide to choose them again an error code is in place to prevent this, making the played choose somewhere else. 

![hit_ship](assets/images/hit_ship.png)

### Gameover

- After the moves are up the game will end. Displaying a message to the user making it clear they can no longer play.

![game_over](assets/images/game_over.png)

### Errors

- Error codes can appear on every area that allows for user input. This was put in place to avoid incorrect characters being used to potentially break the game or even cheat. Below is just one example of an error code and the feedback given to the user on what they should be typing instead.
- If the user enters a coordinate more than once then the terminal will inform the user and ask it to retry.

![errors](assets/images/error_code.png)

## Data Model

I decided to use a Board class as my data model.

The board class stores the board size, the number of ships, the position of the ships, the guesses against the board. It stores the players name too.

This class also has methods to help play the game such as print methods to print out the board and to provide visual aid with text separators.

## Testing

I have manually tested my project by completing the following:
- Passed the code through PEP8 validator and there are no errors showing.
- Given the inputs invalid values, numbers out of bounds, strings instead of integers. They all work fine.
- It was tested numerous times throughout deployment in my own terminal and the Code institute Heroku terminal

## Bugs

- I encountered an issue with using external add ons for fonts, the format kept coming back incorrectly and unreadable. I was not able to fix this and therefore made the decision to leave it out this project.
- I ran into a few code related issues but these were mainly single digit typos or curly braces in the wrong places.
- My original code at the start was not working the way I intended so I decided to rewrite the majority of the code again using points from the code I had already written and this then achieved the desired outcome.

## Validator Testing

- PEP8 was used to check for errors in the code and it returned with no errors or issues.

## Deployment

- This project was deployed using the code Institute mock terminal for Heroku

To deploy your own project:
- Fork or clone this repository
- Create a new Heroku app
- Set the buildbacks to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on deploy

## Credits

- Code Institute for the terminal
- Wikipedia for the details of the game
- ChatGPT helped with error code resolving, pointing out where the error resides from and a potential way to mend it.
- I found another GitHub user by the name 'dmoisset' who had also created a Battleships game in python. I found this user on safari after searching an example of a battlship game. I liked the code that created the board and so I decided to give it my own unique spin on it whilst using the code to set it up.
- The youtuber 'Knowledge Mavens' provided insight into different ways of creating the battleships game. I used part of his code to achieve the outcome I desired. I did then tweak it after to fit in with my code/project.
