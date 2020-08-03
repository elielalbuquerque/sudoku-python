import numpy as np
import copy
from queue import PriorityQueue


class SudokuState:
    def __init__(self, board, heuristic):
        self.board = copy.deepcopy(board)
        self.heuristic = heuristic

    # Retorna uma lista com os novos estados e com as heuristicas de cada um
    def get_next_states(self):
        new_states = []
        new_heuristic_states = self._get_heuristic_states()
        for values, i, j in new_heuristic_states:
            board = copy.deepcopy(self.board)
            heuristic = len(values)
            for value in values:
                board[i][j] = value
                new_state = SudokuState(board, heuristic)
                new_states.append(new_state)
        return new_states

    # Função private para calcular as possibilidades de cada estado
    def _get_heuristic_states(self):
        new_states = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    valid_numbers = self._get_possibilities(i, j)
                    new_state = (valid_numbers, i, j)
                    new_states.append(new_state)
        return new_states

    # Verificas as possibilidades da posição i,j
    def _get_possibilities(self, i, j):
        # Seleciona todos os numeros da linha i
        elem_linha = set(self.board[i, :])
        # Seleciona todos o numeros da coluna j
        elem_coluna = set(self.board[:, j])
        # Seleciona a seção 3x3 que o elemento pertence
        sub_grid = self.get_grid(i, j)
        # Seleciona todos o elementos do dird 3x3
        elem_sub_grid = set(sub_grid.flatten())
        # Todos os valores possiveis.
        all_valid = set(range(10))
        # Operação de conjuntos para saber quais numeros podem preencher a lacuna
        # União de todos os elementos e retirar eles do conjunto de elementos possiveis
        possible_values = all_valid - (elem_sub_grid | elem_coluna | elem_linha)
        return possible_values

    # Funcao para extrar o grid 3x3
    def get_grid(self, grid_row, grid_column):
        sub_grid_linha = grid_row // 3
        sub_grid_coluna = grid_column // 3
        sub_grid = self.board[3 * sub_grid_linha:3 * sub_grid_linha + 3,
                   3 * sub_grid_coluna:  3 * sub_grid_coluna + 3]
        return sub_grid

    # Verifica se o board esta na situação de final
    def is_final(self):
        for i in range(1, 10):
            values = (self.board == i)
            # Checar se não tem numeros repetidos nas linhas ou colunas
            if values.sum(axis=1).max() > 1 or values.sum(axis=0).max() > 1:
                return False
        # Chegar os grids 3x3
        for i in range(3):
            for j in range(3):
                grid = self.get_grid(i, j)
                for n in range(1, 10):
                    # Verifica se não tem numero repetido
                    if (grid == n).sum() > 1:
                        return False
        # Checar se a soma total do tabuleiro é valida
        if self.board.sum() < 9 * 45:
            return False
        return True

    # override do operador "<" para ser usado na priorityQueue
    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __repr__(self):
        return f"Heuristic: {self.heuristic}"


class SudokuPlayer:
    def __init__(self, board):
        self.board = np.array(board)

    # A PriorityQueue sempre retorna quem tiver o menor valor
    # A heuristica usada é a quantidade de numeros que o estado permite.
    def solve_a_star(self):
        frontier = PriorityQueue()
        node = SudokuState(self.board, 1)
        frontier.put(node)
        while not frontier.empty():
            state = frontier.get()
            if state.is_final():
                self.board = state.board
                print(self)
                return state
            # Adicionar os sucessores na PriorityQueue
            for s in state.get_next_states():
                frontier.put(s)
        return None

    # Função que retorna a string com o board
    def __repr__(self):
        out_str = ''
        for i in range(9):
            if i in [3, 6]:
                out_str += '------+-------+------\n'
            line = ''
            for j in range(9):
                if j in [3, 6]:
                    line += '| '
                number = str(self.board[i][j]) if self.board[i][j] > 0 else '_'
                line += number + ' '
            out_str += line + '\n'
        return out_str
