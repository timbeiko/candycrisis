import numpy as np 
import os
import time

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
            print "\n|",
        if currentGame[i] == 'e': 
            print "  |",
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
    indexOfEmpty = currentGame.index('e')
    indexOfMove = ord(move) - 65
    currentGame[indexOfEmpty] = currentGame[indexOfMove] 
    currentGame[indexOfMove] = 'e'
    return currentGame


def main(): 
    # To clear the screen 
    print(chr(27) + "[2J")
    print "Welcome to Candy Crisis\n";
    print "Currently, only the manual mode is available, but come back soon to witness the automated mode!"
    raw_input("Press Enter to continue...")
    print(chr(27) + "[2J")

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
        gameCount += 1

    print "Thank you for playing!"

if __name__ == '__main__':
    main()