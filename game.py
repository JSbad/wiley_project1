import random

# store position coordinates to easily access with the key
positions = {0:(2,1),1:(3,1),2:(3,2),3:(3,3),4:(2,3),5:(1,3),6:(1,2),7:(1,1),8:(2,2)}

# Initialise players and their starting positions
player1 = ['1', 0]
player2 = ['2', 0]

# Get X coordinate
def getXPos(key):
    return positions[key][0]
# Get Y coordinate
def getYPos(key):
    return positions[key][1]
# Handle moving the player position
def movePlayer(player,roll):
    player[1]= player[1]+roll

#move player to starting position  on getting killed
def kill(player):
    movePlayer(player, -player[1])

#roll the Dice
def rollDice():
    return random.randint(1,3)

#display the state of the game
def displayPlane():
    size = 3
    for rows in range(1, size+1):
        for col in range(1,size+1):
            if rows == getXPos(8) and col == getYPos(8):
                print('home\t',end='')
            elif (rows == getXPos(player1[1]) and col== getYPos(player1[1])) and (rows == getXPos(player2[1]) and col== getYPos(player2[1])) and (rows == getXPos(0) and col== getYPos(0)):
                print(player1[0],player2[0],'\t', end='') #allow for both players to be next to each other on start
            elif (rows == getXPos(player1[1]) and col== getYPos(player1[1])):
                print(player1[0],'\t', end='') #display player1
            elif (rows == getXPos(player2[1]) and col== getYPos(player2[1])):
                print(player2[0],'\t', end='') #display player2
            else:
                print('-\t',end='')
        print()

# Display the plane after a player wins the game
def victoryScreen():
    size = 3
    for rows in range(1, size+1):
        for col in range(1,size+1):
            if rows == (getXPos(8) and col == getYPos(8)) and ((rows == getXPos(player1[1]) and col== getYPos(player1[1]))):
                print(player1[0],'\t', end='') #display winning screen for player1
            elif rows == (getXPos(8) and col == getYPos(8)) and ((rows == getXPos(player2[1]) and col== getYPos(player2[1]))):
                print(player2[0],'\t', end='') #display winning screen for player2
            elif (rows == getXPos(player1[1]) and col== getYPos(player1[1])):
                print(player1[0],'\t', end='') #display player1
            elif (rows == getXPos(player2[1]) and col== getYPos(player2[1])):
                print(player2[0],'\t', end='') #display player2
            else:
                print('-\t',end='')
        print()

#Start the game
displayPlane()
while True:
    playerRoll = int(input('Player1 please press 1 to roll the dice'))
    if playerRoll == 1:
        tempRoll = rollDice() #Check value of move before executing it
        if player1[1]+tempRoll>8: #Higher roll than needed to win
            print('Oh no! You have to skip your turn :(')
        elif player1[1]+tempRoll==8: #Winning roll
            movePlayer(player1, tempRoll)
            victoryScreen()
            print('Congratulations Player1! You won!')
            break
        elif player2[1]>player1[1] and (player1[1]+tempRoll) == player2[1]: #kill when caught up to player2
            kill(player2)
            movePlayer(player1, tempRoll)
            print('You just killed player2!')
        else:
            movePlayer(player1, tempRoll)
        displayPlane()
    playerRoll = int(input('Player2 please press 2 to roll the dice'))
    if playerRoll == 2:
        tempRoll = rollDice()
        if player2[1]+tempRoll>8:
            print('Oh no! You have to skip your turn :(')
        elif player2[1]+tempRoll==8:
            movePlayer(player2, tempRoll)
            victoryScreen()
            print('Congratulations Player2! You won!')
            break
        elif player1[1]>player2[1] and (player2[1]+tempRoll) == player1[1]:
            kill(player1)
            movePlayer(player2, tempRoll)
            print('You just killed player1!')
        else:
            movePlayer(player2, tempRoll)
        displayPlane()
    continue