from array import array
import sys
import time
from random import randint
from numpy import *
import os
from colorama import Fore

"""
THESE ARE THE RULES FOR JOHN CONOR'S GAME OF LIFE

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, 
each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). 
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. 
At each step in time, the following transitions occur:
    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:
    Any live cell with two or three live neighbours survives.
    Any dead cell with three live neighbours becomes a live cell.
    All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.
"""

def printGrid(iteration, list_of_lists, m, n):
    os.system('clear')
    print(Fore.BLUE + '\nIteration : '+str(iteration)+'\n')
    for l in range(len(list_of_lists)):
        if l<m:
            for cell in range(len(list_of_lists[l])):
                if cell<n:
                    if list_of_lists[l][cell]=='O':
                        print(Fore.WHITE + list_of_lists[l][cell],end='')
                    else:
                        print(Fore.RED + list_of_lists[l][cell],end='')
            print('\n',end='')

def getCellData(i, j, list_of_lists):
    data = 'O'
    try:
        data = list_of_lists[i][j]
    except:
        data = 'O'
    return data

def updateCellData(i, j, list_of_lists, data):
    list_of_lists[i][j]=data
    return list_of_lists

def convert_custom(data):
    if data=='O':
        return 0
    else :
        return 1

def getPopulation(list_of_lists):
    live_cells = 0
    for l in list_of_lists:
        for cell in l:
            live_cells = live_cells + convert_custom(cell)
    return live_cells

def getLiveCells(index1, index2, list_of_lists):
    live_cells = 0
    live_cells = live_cells + convert_custom(getCellData(index1-1, index2-1, list_of_lists))
    live_cells = live_cells + convert_custom(getCellData(index1, index2-1, list_of_lists))
    live_cells = live_cells + convert_custom(getCellData(index1-1, index2, list_of_lists))
    live_cells = live_cells + convert_custom(getCellData(index1+1, index2-1, list_of_lists))
    live_cells = live_cells + convert_custom(getCellData(index1+1, index2+1, list_of_lists))
    live_cells = live_cells + convert_custom(getCellData(index1+1, index2, list_of_lists))
    live_cells = live_cells + convert_custom(getCellData(index1, index2+1, list_of_lists))
    live_cells = live_cells + convert_custom(getCellData(index1-1, index2+1, list_of_lists))
    return live_cells

def makeFamilyAlive(index1, index2, list_of_lists):
    list_of_lists = updateCellData(index1+1, index2+1, list_of_lists, '*')
    list_of_lists = updateCellData(index1, index2+1, list_of_lists, '*')
    list_of_lists = updateCellData(index1+1, index2, list_of_lists, '*')
    list_of_lists = updateCellData(index1-1, index2-1, list_of_lists, '*')
    list_of_lists = updateCellData(index1, index2-1, list_of_lists, '*')
    list_of_lists = updateCellData(index1-1, index2, list_of_lists, '*')
    list_of_lists = updateCellData(index1-1, index2+1, list_of_lists, '*')
    list_of_lists = updateCellData(index1+1, index2-1, list_of_lists, '*')
    return list_of_lists

def updateGrid(list_of_lists):
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists)):
            live_cells = getLiveCells(i, j, list_of_lists)
            if list_of_lists[i][j]=='*' and (live_cells==2 or live_cells==3):
                list_of_lists[i][j] = '*'
            elif list_of_lists[i][j]=='O' and live_cells==3:
                list_of_lists[i][j] = '*'
            else:
                list_of_lists[i][j] = 'O'
    return list_of_lists

def main():
    try:
        m = int(str(sys.argv[1]).split('x')[0])
        n = int(str(sys.argv[1]).split('x')[1])
    except:
        m = 10
        n = 10
    x = n
    if m>n:
        x = m
    grid_size = x**2
    print('\nWELCOME\n\nIn this game of life, we have '+str(grid_size)+' cells in the configuration of '+str(m)+'X'+str(n)+'\n')
    inner_list = ['O' for i in range(x)]
    outer_list = array([inner_list for i in range(x)])
    
    try :
        where_to_start_1 = int(sys.argv[2])-1
        where_to_start_2 = int(sys.argv[3])-1
    except:
        where_to_start_1 = randint(0,x-1)
        where_to_start_2 = randint(0,x-1)
    # print(where_to_start_1,where_to_start_2)
    print('Point selected to start : '+str(where_to_start_1+1)+','+str(where_to_start_2+1))
    outer_list[where_to_start_1][where_to_start_2] = '*'
    outer_list = updateCellData(where_to_start_1, where_to_start_2, outer_list, '*')
    outer_list = makeFamilyAlive(where_to_start_1, where_to_start_2, outer_list)
    try:
        outer_list = updateCellData(where_to_start_1+4, where_to_start_2, outer_list, '*')
        outer_list = makeFamilyAlive(where_to_start_1+4, where_to_start_2, outer_list)
    except:
        pass
    try:
        outer_list = updateCellData(where_to_start_1-4, where_to_start_2, outer_list, '*')
        outer_list = makeFamilyAlive(where_to_start_1-4, where_to_start_2, outer_list)
    except:
        pass
    try:
        outer_list = updateCellData(where_to_start_1, where_to_start_2+4, outer_list, '*')
        outer_list = makeFamilyAlive(where_to_start_1, where_to_start_2+4, outer_list)
    except:
        pass
    try:
        outer_list = updateCellData(where_to_start_1, where_to_start_2-4, outer_list, '*')
        outer_list = makeFamilyAlive(where_to_start_1, where_to_start_2-4, outer_list)
    except:
        pass
    printGrid(0, outer_list, m, n)
    StartingPopulation = getPopulation(outer_list)
    try:
        iterations = int(sys.argv[4])
    except:
        iterations = 10

    for i in range(iterations):
        outer_list = updateGrid(outer_list)
        printGrid(i+1, outer_list, m, n)
        time.sleep(0.1)
    LatestPopulation = getPopulation(outer_list)
    print('Starting population : '+str(StartingPopulation))
    print('Current population : '+str(LatestPopulation))
main()

"""
Some observations:
Constant after some iterations : python3 game.py 25x50 12 25 50
Constant after a single iteration : python3 game.py 25x50 12 29 50

"""