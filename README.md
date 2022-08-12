# Python Ludo Game

## Getting started
   To play, simply download the Python file, execute it and follow instructions!  

### Variables

•	**positions** – a dictionary of coordinates with corresponding keys ranging from 0 to 8 where 0 is the starting position and 8 is the finish  
•	**player1, player2** – lists responsible for storing the identifiers of the players and their current positions, initialised with 0  
•	playerRoll – used to switch between logic of the players depending on the current player  
•	tempRoll – used to store the value of the dice roll in order to verify whether the move is legal, kills someone, wins or is out of bounds  


### Functions

•	**getXPos, getYPos** – get X and Y coordinates of the position from the dictionary based on provided key  
•	**movePlayer** – moves specified player forward roll number of steps  
•	**kill** – calls the movePlayer function specifying the negative value of their current position, effectively placing them at the start node  
•	**displayPlane** – asserts the X and Y axis, displays the home at the final node,  
  the players at the starting position and after their coordinates have updated and fills all empty nodes with dashes  
•	**victoryScreen** – displays the screen with the final position of the players with the winning player in the house  
•	**The main loop** – starts from player1, prompts input and rolls the dice to then check conditions.  
  Skips turn if the move is out of bounds, displays victory screen and exits the loop on success,  
  kills the other player if the current one’s position was lower than theirs and moves to that position,  
  or proceeds with the regular move forward, after which it displays the updated plane and moves onto player2 with the same steps,  
  upon completion of which redirects to the beginning of the loop.  


