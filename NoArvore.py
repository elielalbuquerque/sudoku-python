#Classe que mantém os nós com os problemas e seus respectivos estados
class NoArvore:
    def __init__(self, estado, operacao=None):
        self.estado = estado
        self.operacao = operacao

    # Usa cada operacao para criar um novo estado do quadro
    def expandir(self, problema):
        return [self.no_filho(problema, operacao)
                for operacao in problema.operacoes(self.estado)]

    # Retorna o No com o novo estado do quadro
    def no_filho(self, problema, operacao):
        next = problema.resultado(self.estado, operacao)
        return NoArvore(next, operacao)
