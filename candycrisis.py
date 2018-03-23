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

def boardAsString(currentGame):
    s = ""
    for i in range(0,15):
        if i % 5 == 0:
            s += "\n|"
        if currentGame[i] == 'e': 
            s += "  |"
        else:
            s += currentGame[i] + " |"
    return s

def validMove(move, currentGame):
    index = currentGame.index('e')
    emptyLetter = chr(index + 65)
    return (move in VALID_MOVES[emptyLetter])

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
    # Use gc instead of 'gameConfig' because things are passed by reference
    # and the 'dc' function will create a copy we can play with in the function
    gc = dc(gameConfig)

    # Heuristic 0: return 0
    # return 0 

    # Heuristic 1: return the 5 minus the number of matching candies in rows 1 & 3 
    # i = 0 
    # j = 10 
    # match = 0 
    # while i < 5: 
    #     if gc[i] == gc[j]:
    #         match += 1 
    #     i += 1 
    #     j += 1  
    # return (5 - match)*10.0 

    # Heuristic 2: like 1, and +1 point if 'e' is in the top or bottom row 
    # Slower than heuristic 1 for novice inputs
    # i = 0 
    # j = 10 
    # match = 0 
    # while i < 5: 
    #     if gc[i] == gc[j]:
    #         match += 1 
    #     elif gc[i] == 'e' or gc[j] == 'e':
    #         match += 1
    #     i += 1 
    #     j += 1  
    # return 6 - match 

    # Heuristic 3: like 1, but multiplied by 10. 
    # Much quicker than H1
    i = 0 
    j = 10 
    match = 0 
    while i < 5: 
        if gc[i] == gc[j]:
            match += 1 
        i += 1 
        j += 1  
    return (5 - match)*10.0 

def outputGameInfo(gameCount, time, moves, output_file="outputs.txt"):
    with open(output_file, "a") as f:
        # Number of the game - not needed in output
        # f.write("Game " + str(gameCount) + "\n")
        # Moves Played
        for move in moves:
            f.write(move)
        f.write("\n")
        # Time to complete
	milliTime = time*1000 
        f.write(str(milliTime) + "ms\n")

def outputGameMoves(gameCount, moves, currentGame):
    moveFile = "moves/game" + str(gameCount) + "moves.txt"
    gameBoard = dc(currentGame)

    with open(moveFile, "w") as f: 
        f.write("Game " + str(gameCount) + "\n")
        f.write("Initial Board:\n")
        f.write(boardAsString(gameBoard) + "\n\n")

        for move in moves: 
            f.write(move)
            gameBoard = moveCandy(move, gameBoard)
            f.write(boardAsString(gameBoard) + "\n\n")

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
    # Get number of input file from user
    fileNum = raw_input("Please input a number between 1-4 to specify which input file to use: ")
    output_file = "output" + str(fileNum) + ".txt"
    # Get initial configurations from the input file 
    readConfigs("input" + str(fileNum) + ".txt") 
    # Clear output file from previous games 
    open(output_file, "w")

    # MAIN GAME LOOP
    gameCount = 1
    totalMovesPlayed = 0
    startOfAllGames = time.time()
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
                outputGameInfo(gameCount, time.time() - startTime, currentNode.path, output_file)
                outputGameMoves(gameCount, currentNode.path, currentGame)
                break 

            # Get letter corresponding to empty tile, and it's next moves            
            index = currentNode.config.index('e')
            emptyLetter = chr(index + 65)
            nextMoves = VALID_MOVES[emptyLetter]

            # Iterate over possible next mvoes 
            for move in nextMoves: 
                g_n = currentNode.G + 1 
                moveConfig = moveCandy(move, currentNode.config) # Board after playing move 

                addToOpen = True 
                checkClosedList = True 

                # COMMENTED THIS OUT: it actually slows things down! 
                # Don't add if in openlist with <= G(n)
                # for node in openlist: 
                #     if node.config == moveConfig: 
                #         if node.G <= g_n: 
                #             addToOpen = False 
                #             checkClosedList = False 
                #             break 

                # Don't add if in closedlist with <= G(n)
                if checkClosedList:
                    for node in closedlist: 
                        if node.config == moveConfig: 
                            if node.G <= g_n: 
                                addToOpen = False 
                                break 

                # Add to open list if none of the two conditions above apply 
                if addToOpen: 
                    moveNode = Node(currentNode, moveConfig, g_n, heuristic(moveConfig), currentNode.path + move)
                    openlist.append(moveNode)
            closedlist.append(currentNode)

        # increment game count     
        gameCount += 1 

    # Output total moves played and total time taken
    totalTimeTaken = time.time() - startOfAllGames
    print totalMovesPlayed 
    print totalTimeTaken

    with open(output_file, "a") as f:
        f.write(str(totalMovesPlayed) + "\n")
       #  f.write("Total time taken: " + str(totalTimeTaken))

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
