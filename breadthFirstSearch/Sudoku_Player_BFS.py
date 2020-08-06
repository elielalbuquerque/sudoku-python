
from queue import Queue
from breadthFirstSearch.No_Arvore import NoArvore
from breadthFirstSearch.Sudoku_State_BFS import SudokuStateBFS


#Função que varre a arvore de problemas em busca de uma solução válida para o problema do SUDOKU
class SudokuPlayerBFS:
    def __init__(self, board):
        self.board = SudokuStateBFS(board)
        self.steps = 0

    def busca_em_largura(self):
        # Cria o nó inicial da árvore de problemas mantendo o quadro original
        no = NoArvore(self.board.inicial)
        # Verifi se o quadro incial está correto e retorna imediatamente se este é válido
        if self.board.testa_validade(no.estado):
            return no

        fronteira = Queue()
        fronteira.put(no)

        # Executa até todos os nós forem explorados e uma solução for encontrada
        while (fronteira.qsize() != 0):
            no = fronteira.get()
            for filho in no.expandir(self.board):
                self.steps += 1
                if self.board.testa_validade(filho.estado):
                    return filho.estado
                fronteira.put(filho)
        return None

    # Função que retorna o número de passos
    def get_steps(self):
        return self.steps



