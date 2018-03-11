import numpy as np 
import os
import time
from Node import Node 
from copy import deepcopy as dc 

# for debugging 
# import pdb; pdb.set_trace()

INITIAL_GAME_CONFIGS = []
output_file = 'outputs.txt'
LETTER_BOARD = ['A', 'B', 'C', 'D', 'E', 
                'F', 'G', 'H', 'I', 'J', 
                'K', 'L', 'M', 'N', 'O']

VALID_MOVES = {
    'A': ['B', 'F', 'G'], 
    'B': ['A', 'G', 'C'], 
    'C': ['B', 'D', 'H'],
    'D': ['C', 'I', 'E'],
    'E': ['D', 'J'],
    'F': ['A', 'G', 'K'],
    'G': ['B', 'F', 'L', 'H'],
    'H': ['C', 'G', 'M', 'I'], 
    'I': ['D', 'H', 'N', 'J'], 
    'J': ['I', 'E', 'O'], 
    'K': ['F', 'L'], 
    'L': ['G', 'K', 'M'], 
    'M': ['L', 'H', 'N'], 
    'N': ['M', 'I', 'O'], 
    'O': ['N', 'J']
}

def readConfigs(inputFile): 
    inputs = open(inputFile, 'r')
    for line in inputs:
        INITIAL_GAME_CONFIGS.append(line)

def printBoard(currentGame):
    for i in range(0,15):
        if i % 5 == 0:
            print ("\n|"),
        if currentGame[i] == 'e': 
            print ("  |"),
        else:
            print currentGame[i] + " |",

def validMove(move, currentGame):
    index = currentGame.index('e')
    emptyLetter = chr(index + 65)
    return (move in VALID_MOVES[emptyLetter])

def outputGameInfo(gameCount, time, moves):
    with open(output_file, "a") as f:
        # Number of the game
        f.write("Game " + str(gameCount) + "\n")
        # Moves Played
        for move in moves:
            f.write(move)
        f.write("\n")
        # Time to complete 
        f.write(str(time) + " seconds\n\n")

def checkIfGameWon(currentGame):
    i = 0
    j = 10
    while i < 5: 
        if currentGame[i] != currentGame[j]:
            return False 
        i += 1
        j += 1 
    return True 

def moveCandy(move, currentGame):
    # Important to make a copy of currentGame otherwise 
    # when doing automatic mode, it will keep updating the currentNode and not its children
    gameCopy = dc(currentGame);
    indexOfEmpty = gameCopy.index('e')
    indexOfMove = ord(move) - 65
    gameCopy[indexOfEmpty] = gameCopy[indexOfMove] 
    gameCopy[indexOfMove] = 'e'
    return gameCopy

def heuristic(gameConfig):
    return 0 

def manual_mode():
    print "To choose your next move, simply type the letter corresponding to the candy you want to move in the empty space."
    print "A board showing the letters for each position will be displayed underneath the game board."
    print "Be quick! You are timed!"
    raw_input("Press Enter to continue...")
    print(chr(27) + "[2J")

    # Get initial configurations from the input file 
    readConfigs('inputs.txt') 
    # Clear output file from previous games 
    open(output_file, "w")

    # MAIN GAME LOOP
    gameCount = 1
    totalMovesPlayed = 0
    for gameConfig in INITIAL_GAME_CONFIGS:  # Iterate over all games in input file
    # Variables for the current game 
        startTime = time.time()
        movesPlayed = []
        currentGame = gameConfig.split()

        # Single game loop 
        while True: 
            print "Game: " + str(gameCount)
            printBoard(currentGame) 
            print 
            printBoard(LETTER_BOARD)
            print

            # Single move loop 
            while True: 
                move = raw_input("Enter a letter between A and O: ")
                move = move.upper()

                # String too long or too short 
                if len(move) != 1: 
                    continue    
                # Valid character  
                elif ord(move) >= 65 and ord(move) < 80:
                    if validMove(move, currentGame):
                        currentGame = moveCandy(move, currentGame)
                        movesPlayed.append(move)
                        break
                    else: 
                        print "Invalid move. Please choose a letter corresponding to a tile adjacent to the empty one."
                # Invalid character
                else:
                    print "\nThat is not a letter between A and O. Try again."

            currentGame = moveCandy(move, currentGame)
            if checkIfGameWon(currentGame):
                # Get total time of game 
                totalTime = time.time() - startTime

                print(chr(27) + "[2J")
                print "Game Won!"
                print "Final game board:"
                printBoard(currentGame)
                print
                raw_input("Press Enter to continue...")
                break 

        # Clear screen 
        print(chr(27) + "[2J")

        # End of current game 
        print "\n"                              
        outputGameInfo(gameCount, totalTime, movesPlayed) 
        totalMovesPlayed += len(movesPlayed)
        gameCount += 1

    with open(output_file, "a") as f:
        f.write("Total moves played: " + str(totalMovesPlayed))
    return True

def automatic_mode():
    # Get initial configurations from the input file 
    readConfigs('inputs.txt') 
    # Clear output file from previous games 
    open(output_file, "w")

    # MAIN GAME LOOP
    gameCount = 1
    totalMovesPlayed = 0
    for gameConfig in INITIAL_GAME_CONFIGS:  # Iterate over all games in input file
        print "Game " + str(gameCount)

        # Variables for the current game 
        movesPlayed = []
        currentGame = gameConfig.split()
        openlist = []
        closedlist = []
        startTime = time.time()

        # Use first empty node as root of tree
        rootNode = Node(None, currentGame, 0, heuristic(currentGame), "")
        openlist.append(rootNode)

        # Loop until openlist is empty 
        while len(openlist) != 0: 
            openlist = sorted(openlist, key=lambda n: n.F) # Sort open list by f(n)
            currentNode = openlist.pop(0) # Get lowest value of open list

            # Check if the game is won, if so, output game information 
            if checkIfGameWon(currentNode.config):
                print currentNode.path
                printBoard(currentNode.config)
                print
                print str(time.time() - startTime) + " seconds"
                print

                totalMovesPlayed += len(currentNode.path)
                outputGameInfo(gameCount, time.time() - startTime, currentNode.path)
                # outputGameMoves(gameCount, currentNode.path, )
                break 

            # Get letter corresponding to empty tile, and it's next moves            
            index = currentNode.config.index('e')
            emptyLetter = chr(index + 65)
            nextMoves = VALID_MOVES[emptyLetter]

            # Iterate over possible next mvoes 
            for move in nextMoves: 
                g_n = currentNode.G + 1 
                moveConfig = moveCandy(move, currentNode.config) # Board after playing move 

                # Create node for move - would probably be better to do this after the checks below.
                moveNode = Node(currentNode, moveConfig, g_n, heuristic(moveConfig), currentNode.path + move)

                addToOpen = True
                # Don't add node to openlist if there is a shorter path to the same config 
                if moveNode in openlist:
                    if moveNode.G <= g_n: 
                        addToOpen = False 

                # Don't add a node to the closed list if we've visited the same config 
                # from a shorter path before 
                if moveNode in closedlist:
                    if moveNode.G <= g_n: 
                        addToOpen = False 

                # Add to open list if none of the two conditions above apply 
                if addToOpen: 
                    openlist.append(moveNode)
            closedlist.append(currentNode)

        # increment game count     
        gameCount += 1 

    # Output total moves played 
    print totalMovesPlayed 
    with open(output_file, "a") as f:
        f.write("Total moves played: " + str(totalMovesPlayed))

def main(): 
    # To clear the screen 
    print(chr(27) + "[2J")

    print "Welcome to Candy Crisis\n";
    print ("A : Manual Mode")
    print("B : Automatic Mode")
    user_input = raw_input("Please enter something: ")
    print("You entered " + str(user_input))
    raw_input("Press Enter to continue...")
    print(chr(27) + "[2J")
    
    if (user_input.upper() == "A"):
        result = manual_mode()
        if (result == True):
            print ("Thank you for playing!")
        else:
            print ("Sorry Manual Mode Failed. Try Again" ) 
    else:
        result = automatic_mode()

if __name__ == '__main__':
    main()