
from queue import Queue
from breadthFirstSearch.Tree_Node import TreeNode
from breadthFirstSearch.Sudoku_State_BFS import SudokuStateBFS


# Classe que possui as funcionalidades que varrem a arvore de
# problemas em busca de uma solução válida para o problema do SUDOKU
class SudokuPlayerBFS:
    def __init__(self, board):
        self.board = SudokuStateBFS(board)
        self.steps = 0

    def breadth_first_search(self):
        # Cria o nó inicial da árvore de problemas mantendo o quadro original
        node = TreeNode(self.board.start)
        # Verifi se o quadro incial está correto e retorna imediatamente se este é válido
        if self.board.test_validity(node.state):
            return node

        border = Queue()
        border.put(node)

        # Executa até todos os nós forem explorados e uma solução for encontrada
        while (border.qsize() != 0):
            node = border.get()
            for children in node.expand(self.board):
                self.steps += 1
                if self.board.test_validity(children.state):
                    return children.state
                border.put(children)
        return None

    # Função que retorna o número de passos
    def get_steps(self):
        return self.steps



