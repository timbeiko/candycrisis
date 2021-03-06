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
    indexOfEmpty = currentGame.index('e')
    indexOfMove = ord(move) - 65
    currentGame[indexOfEmpty] = currentGame[indexOfMove] 
    currentGame[indexOfMove] = 'e'
    return currentGame



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

    return True

 #automatic mode   
 #i wanted to initialize values here, not sure   
 def __init__(self,value,point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0
    def move_cost(self,other):
        return 0 if self.value == '.' else 1
def manhattan(point,point2):
    return abs(point.point[0] - point2.point[0]) + abs(point.point[1]-point2.point[0])


def automatic_mode():
     #The open and closed sets
    openset = set()
    closedset = set()
    #Current point is the starting point
    current = 'A'
    #Add the starting point to the open set
    openset.add(current)
    #While the open set is not empty
    while openset:
        #Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o:o.G + o.H)
        #If it is the item we want, retrace the path and return it
        if checkIfGameWon(currentGame):
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        #Remove the item from the open set
        openset.remove(current)
        #Add it to the closed set
        closedset.add(current)
        #Loop through the node's children/siblings
        for node in VALID_MOVES:
            #If it is already in the closed set, skip it
            if node in closedset:
                continue
            #Otherwise if it is already in the open set
            if node in openset:
                #Check if we beat the G score 
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                #Set the parent to our current item
                node.parent = current
                #Add it to the set
                openset.add(node)
    #Throw an exception if there is no path

    return True  

def main(): 
    # To clear the screen 
    print(chr(27) + "[2J")
    print "Welcome to Candy Crisis\n";
    print "Currently, only the manual mode is available, but come back soon to witness the automated mode!"
    print ("A : Manual Mode")
    print("B : Automatic Mode")
    user_input = raw_input("Please enter something: ")
    print("You entered " + str(user_input))
    raw_input("Press Enter to continue...")
    print(chr(27) + "[2J")
    
    if (user_input == "A"):
        result = manual_mode()
        if (result == True):
            print ("Thank you for playing!")
        else:
            print ("Sorry Manual Mode Failed. Try Again" ) 
    else:
        result = automatic_mode()
                          

if __name__ == '__main__':
    main()