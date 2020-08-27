#Classe que mantém os nós com os problemas e seus respectivos estados
class TreeNode:
    def __init__(self, state, operation=None):
        self.state = state
        self.operation = operation

    # Usa cada operacao para criar um novo estado do quadro
    def expand(self, problem):
        return [self.children_node(problem, operation)
                for operation in problem.operations(self.state)]

    # Retorna o No com o novo estado do quadro
    def children_node(self, problem, operation):
        next = problem.result(self.state, operation)
        return TreeNode(next, operation)
