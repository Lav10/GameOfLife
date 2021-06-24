# GameOfLife
 
This is a single piece of code which make it easy for anyone visualize the working of "Conway's Game of Life" in just a terminal using Python3

For full details on Conway's Game of Life, please refer this wikipedia article : https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# Rules
Following are the rules for Conway's Game of Life :
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.
The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

# Input 
python3 game.py mxn x y iterations

mxn is the configuration of the world which will form the world for this game
m is the number of rows
n is the number of columns
x is the number of row in which you want to place your population base
y is the number of column in which you want to place your population base
iterations is the number of times the grid will be updated based on the rules for Conway's Game of Life

# Working
A fixed colony pattern of 45 population will be populated on coordinates x,y
The world will be of configuration ZxZ where Z is the greater value from m and n
mxn is the window size which will be printed on the terminal from ZxZ world
After placing the fixed colony, the game will start and will update and print the grid by following the rules for Conway's Game of Life
Once the number of iterations matches the user given iteration, the game will stop and the population at that start and end will be printed

# Dependency
Python non-native libraries dependency : numpy and colorama