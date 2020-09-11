#!/usr/bin/env python3
"""
Sudoku - Codificação paara resolução do Sudoku usando a lógica
do algorirmo de busca em largura e a busca em largura com heurística
baseada no algoritmo A*.
Autores : Gustavo Zanatta Bruno e Guilherme F. S. Camnpos
"""
import sys
import time
import numpy
from breadthFirstSearch.Sudoku_Player_BFS import SudokuPlayerBFS
import input_output as i_o
from aStar.Sudoku_A_Star import SudokuPlayerAStar
import pandas as pd
import matplotlib.pyplot as plt

def breadth_first_search(debug=True):
    if debug: print('Resolvendo com a busca em largura...')
    t1 = time.time()
    sudoku_bfs = SudokuPlayerBFS(initial_board.tolist())
    result = numpy.asarray(sudoku_bfs.breadth_first_search(), dtype=numpy.int32)
    s = sudoku_bfs.get_steps()
    elapsed_time = time.time() - t1
    if debug: i_o.print_result(result, time.time() - t1, s)
    return elapsed_time

def a_star_search(debug=True):
    if debug: print('Resolvendo com a Heurística A-Star...')
    t1 = time.time()
    sudoku_A_Star = SudokuPlayerAStar(initial_board)
    result = numpy.asarray(sudoku_A_Star.solve_a_star(), dtype=numpy.int32)
    s = sudoku_A_Star.get_steps()
    elapsed_time = time.time() - t1
    if debug: i_o.print_result(result, time.time() - t1, s)
    return elapsed_time


initial_board = i_o.convert_txt_to_array('input.txt')

while True:
    print("Opções de algoritmos para resolver o SUDOKU:")
    print("1- Algoritmo de Busca em Largura")
    print("2- Busca Heurística A-Star")
    print("3- Todos")
    print("0- Sair")
    try:
        option = int(input("Enter a number: "))
        if option < 0 or option > 5:
            raise Exception
    except:
        continue

    if option == 1:
        breadth_first_search()
    elif option == 2:
        a_star_search()
    elif option == 3:
        breadth_first_search()
        a_star_search()
    elif option == 4:
        print("Iniciando a execução dos algoritmos 100 vezes.")
        bfs_runs = []
        a_star_runs = []
        for i in range(100):
            elapsed_bfs = breadth_first_search(False)
            bfs_runs.append(elapsed_bfs)
            elapsed_a_star = a_star_search(False)
            a_star_runs.append(elapsed_a_star)
        df = pd.DataFrame(zip(bfs_runs, a_star_runs), columns=['Busca em largura', 'Busca heurística A*'])
        print(df.describe())
        df.boxplot('Busca em largura', grid=False)
        plt.ylabel('Tempo de execução (s)')
        plt.savefig('bfs_boxplot.png')
        plt.show()
        df.boxplot('Busca heurística A*', grid=False)
        plt.ylabel('Tempo de execução (s)')
        plt.savefig('a_star_boxplot.png')
        plt.show()
    elif option == 0:
        sys.exit(0)