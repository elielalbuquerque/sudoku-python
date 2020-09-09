import numpy as np
import copy
from queue import PriorityQueue

passos = 0

class SudokuStateAStar:
    def __init__(self, board, heuristic, depth=0):
        self.board = copy.deepcopy(board)
        self.heuristic = heuristic
        self.depth = depth

    def get_heuristic(self):
        return self.heuristic - self.depth * 10

    # Retorna uma lista com os novos estados e com as heuristicas de cada um
    def get_next_states(self):
        depth = self.depth + 1
        new_states = []
        new_heuristic_states = self._get_heuristic_states()
        for values, i, j in new_heuristic_states:
            board = copy.deepcopy(self.board)
            heuristic = len(values)
            for value in values:
                board[i][j] = value
                new_state = SudokuStateAStar(board, heuristic, depth)
                new_states.append(new_state)
        sorted_states = sorted(new_states)
        if sorted_states:
            if len(sorted_states) > 1:
                if sorted_states[0].get_heuristic() == sorted_states[1].get_heuristic():
                    return sorted_states[:2]
            return sorted_states[:1]
        return new_states

    # Função private para calcular as possibilidades de cada estado
    def _get_heuristic_states(self):
        new_states = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    valid_numbers = self._get_possibilities(i, j)
                    new_state = (valid_numbers, i, j)
                    yield new_state
                    #new_states.append(new_state)
        #return new_states

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

    def testa_validade(self):
        state = self.board
        tipo = 9
        altura = 3

        # Soma esperada de cada linha, coluna ou quadrante.
        total = sum(range(1, tipo+1))

        # Checa linhas e colunas e retorna falso se o total não é valido
        for linha in range(tipo):
            if (len(state[linha]) != tipo) or (sum(state[linha]) != total):
                return False

            total_coluna = 0
            for coluna in range(tipo):
                total_coluna += state[coluna][linha]

            if (total_coluna != total):
                return False

        # Verifica os quadrantes e retorna falso se o total é inválido
        for coluna in range(0,tipo,3):
            for linha in range(0,tipo,altura):

                total_quadrante = 0
                for linha_quadrante in range(0,altura):
                    for coluna_quadrante in range(0,3):
                        total_quadrante += state[linha + linha_quadrante][coluna + coluna_quadrante]

                if (total_quadrante != total):
                    return False
        return True

    # override do operador "<" para ser usado na priorityQueue
    def __lt__(self, other):
        return self.get_heuristic() < other.get_heuristic()

    def __repr__(self):
        return f"Heuristic: {self.get_heuristic()}"


class SudokuPlayerAStar:
    def __init__(self, board):
        self.board = np.array(board)
        self.steps = 0


    # A PriorityQueue sempre retorna quem tiver o menor valor
    # A heuristica usada é a quantidade de numeros que o estado permite.
    def solve_a_star(self):
        frontier = PriorityQueue()
        node = SudokuStateAStar(self.board, 1)
        frontier.put(node)
        while not frontier.empty():
            state = frontier.get()
            #if state.is_final():
            if state.testa_validade():
                self.board = state.board
                #print(self)
                return self.board
            # Adicionar os sucessores na PriorityQueue
            for s in state.get_next_states():
                self.steps += 1
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

    # Função que retorna o número de passos
    def get_steps(self):
        return self.steps