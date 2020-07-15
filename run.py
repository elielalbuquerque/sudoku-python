#!/usr/bin/env python3
"""
Sudoku - Solve sudoku with Python using CSF, DFS and Backtracking approach
Based on codes writen by Hamidreza Mahdavipanah (@mahdavipanah) and Michael Zietz (@zietzm)
Author : Gustavo Zanatta Bruno e Guilherme F. S. Camnpos
Repository: https://github.com/zanattabruno/sudoku-ia-unisinos
License : MIT License
"""
import sys
import time

import numpy as np

import dfs
import simple_backtracking
import mrv_backtracking

import input as inp

result = None

def print_board(res, t, s=0):
    if res is None:
        print("This sudoku is not solvable!")
    else:
        print(res)
        print(f'Time to solve: {t} seconds!')
        print(f'Steps {s}!\n')
        try:
            with open('output.txt', 'w') as file:
                file.write(res)
        except:
            pass

def option_1():
    print('Calculating Depth-first search...')
    t1 = time.time()
    b = dfs.DepthFirstSearch(sudoku)
    b.solve()
    result=b.board
    t2 = time.time() - t1
    print_board(result,t2,b.num_steps)

def option_2():
    print('Calculating Simple backtracking...')
    t1 = time.time()
    result = np.asarray(simple_backtracking.search(sudoku.tolist()), dtype=np.int32)
    s = simple_backtracking.get_steps()
    t2 = time.time() - t1
    print_board(result,t2,s)

def option_3():
    print('Calculating Backtracking with MRV heuristic...')
    t1 = time.time()
    result = np.asarray(mrv_backtracking.search(sudoku.tolist()), dtype=np.int32)
    s = mrv_backtracking.get_steps()
    t2 = time.time() - t1
    print_board(result,t2,s)

f = open("input.txt", "r")
sudoku = inp.covert_txt_to_array(f)

while True:
    print("Algorithms options to solve Sudoku:")
    print("    1- Depth-first search")
    print("    2- Simple backtracking")
    print("    3- Backtracking with MRV heuristic")
    print("    4- All")
    print("    0- Exit")
    try:
        option = int(input("Enter a number: "))
        if option < 0 or option > 4:
            raise Exception
    except:
        continue

    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()
    elif option == 4:
        option_1()
        option_2()
        option_3()
    elif option == 0:
        sys.exit(0)




