import numpy as np 
import os

INITIAL_GAME_CONFIGS = []
output_file = 'outputs.txt'
LETTER_BOARD = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

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

# To be implemented
def validMove(move):
    return True

def outputGameInfo(gameCount, time, moves):
    with open(output_file, "a") as f:
        # Number of the game
        f.write("Game " + str(gameCount) + "\n")
        # Moves Played
        for move in moves:
            f.write(move)
        f.write("\n")
        # Time to complete 
        f.write(str(time) + "ms\n\n")




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
        print "Game: " + str(gameCount)
        currentGame = gameConfig.split()
        printBoard(currentGame) 
        print 
        printBoard(LETTER_BOARD)
        print

        while True: 
            move = raw_input("Enter a letter between A and O: ")

            # String too long or too short 
            if len(move) != 1: 
                continue    
            # Valid character  
            elif ord(move.upper()) >= 65 and ord(move.upper()) < 80:
                if validMove(move):
                    break 
            # Invalid character
            else:
                print "\nThat is not a letter between A and O. Try again."

        # Clear screen  
        print(chr(27) + "[2J")

        # End of current game 
        print "\n"
        outputGameInfo(gameCount, 234, ['A', 'B', 'C', 'D', 'E'])
        gameCount += 1

    print "Thank you for playing!"

if __name__ == '__main__':
    main()