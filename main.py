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

import simple_backtracking
import mrv_backtracking
import bfs
import dfs


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

def calc_dfs():
    print('Calculating Depth-first search...')
    t1 = time.time()
    result = np.asarray(dfs.solve_dfs(sudoku.tolist()), dtype=np.int32)
    s = dfs.get_steps()
    t2 = time.time() - t1
    print_board(result,t2,s)

def calc_bfs():
    print('Calculating Breadth-first search...')
    t1 = time.time()
    result = np.asarray(bfs.solve_bfs(sudoku.tolist()), dtype=np.int32)
    s = bfs.get_steps()
    t2 = time.time() - t1
    print_board(result,t2,s)

def calc_simple_backtracking():
    print('Calculating Simple backtracking...')
    t1 = time.time()
    result = np.asarray(simple_backtracking.search(sudoku.tolist()), dtype=np.int32)
    s = simple_backtracking.get_steps()
    t2 = time.time() - t1
    print_board(result,t2,s)

def calc_backtracking_mrv():
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
    print("    1- Breadth-first search")
    print("    2- Depth-first search")
    print("    3- Simple backtracking")
    print("    4- Backtracking with MRV heuristic")
    print("    5- All")
    print("    0- Exit")
    try:
        option = int(input("Enter a number: "))
        if option < 0 or option > 5:
            raise Exception
    except:
        continue

    if option == 1:
        calc_bfs()
    elif option == 2:
        calc_dfs()
    elif option == 3:
        calc_backtracking_mrv()
    elif option == 4:
        calc_backtracking_mrv()
    elif option == 5:
        calc_dfs()
        calc_bfs()
        calc_simple_backtracking()
        calc_backtracking_mrv()
    elif option == 0:
        sys.exit(0)




