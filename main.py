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
import entrada_saida as e_s
from aStar.Sudoku_A_Star import SudokuPlayerAStar

def busca_em_largura():
    print('Resolvendo com a busca em largura...')
    t1 = time.time()
    sudoku_bfs = SudokuPlayerBFS(quadro_inicial.tolist())
    result = numpy.asarray(sudoku_bfs.breadth_first_search(), dtype=numpy.int32)
    s = sudoku_bfs.get_passos()
    e_s.imprime_resultado(result, time.time() - t1, s)

def busca_a_star():
    print('Resolvendo com a Heurística A-Star...')
    t1 = time.time()
    sudoku_A_Star = SudokuPlayerAStar(quadro_inicial)
    result = numpy.asarray(sudoku_A_Star.solve_a_star(), dtype=numpy.int32)
    s = sudoku_A_Star.get_steps()
    e_s.imprime_resultado(result, time.time() - t1, s)


quadro_inicial = e_s.coverte_txt_to_array('entrada.txt')

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
        busca_em_largura()
    elif option == 2:
        busca_a_star()
    elif option == 3:
        busca_em_largura()
        busca_a_star()
    elif option == 0:
        sys.exit(0)