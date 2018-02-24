# Candy Crisis
Semester project for COMP472.

The main file for this project is `candycrisis.py`

To run this on the lab machines at Concordia (Linux) you will need to run the following command: `module load python/2.7.10`

### Second deliverable (Mar. 15)
Automatic Mode
(e.g. implementation of the search, output file generation, programming quality…) 

#### TODOs

- [x] Refactor current code to let user choose between manual and automatic mode 
- [ ] For automatic mode, output intermediate screens to file rather than on-screen 
  - Perhaps save them in memory and only output at the end of the game ? 
- [ ] Save & output the total number of moves it took to solve all the puzzles of the input file 
- [ ] Choose heuristic to implement
- [ ] Decide "how deep" to search at each turn / what algorithm to use 
- [ ] ??? 

### First deliverable (Feb. 15)
Manual entries + Functionality of the rules of the game
(e.g. visual trace after each move, detection of illegal moves, programming quality…) 

## Game description 
#### Input:
Your program will read a series of initial configurations from a text file, where each line will represent an initial configuration. Each candy type will be represented by a unique character (‘r’, ‘b’, ‘w’, ‘y’, ‘g’ or ‘p’) and the empty slot will be indicated by the character ‘e’. For example, the line:
e r r r r r b w b b w y b r y represents the first puzzle given on the previous page
(empty at position A, Reese’s Pieces at positions B, C, D, E, F,
a Bazooka Bubble Gum at G, a Walnetto at H, ...)

#### Play Modes
Your program should be able to run in manual mode and in automatic mode. This means that you should be able to run your program with:
1. Manual entry for the player, i.e. a human indicating the moves by hand.
  Note that if a human enters an illegal move, your program should give a warning and allow the user to enter a new move.
2. Automatic mode, i.e. your “AI” solving and indicating the moves.
  Note that if your program generates an illegal move, the entire puzzle solution will be considered wrong.

After each move, your program must display the new configuration of the candy box.

#### Output:
Your program must output:
1- A set of puzzle solutions: Your program must produce an output file, which contains, for each puzzle of the input file:
a) the sequence of moves necessary to solve the puzzle,
b) the time (real time in milliseconds in the lab’s desktops) required to solve the puzzle
c) In addition, at the end of the output file, you must indicate:
d) the total number of moves it took to solve all the puzzles of the input file
2- A visual trace: In addition to the puzzle solutions, for each puzzle, your program must also display on the screen (or
in another output file) the configuration of the candy box after each move. 
