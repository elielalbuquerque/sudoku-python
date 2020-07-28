from queue import Queue
#import time
from SudokuBuscaEmLargura import *
from NoArvore import *

passos = 0



#Função que varre a arvore de problemas em busca de uma solução válida para o problema do SUDOKU
def Busca_em_largura(problema):
    # Cria o nó inicial da árvore de problemas mantendo o quadro original
    no = NoArvore(problema.inicial)
    # Verifi se o quadro incial está correto e retorna imediatamente se este é válido
    if problema.teste_validade(no.estado):
        return no

    fronteira = Queue()
    fronteira.put(no)

    # Executa até todos os nós forem explorados e uma solução for encontrada
    global passos
    passos = 0
    while (fronteira.qsize() != 0):
        no = fronteira.get()
        for filho in no.expandir(problema):
            passos += 1
            if problema.teste_validade(filho.estado):
                return filho

            fronteira.put(filho)

    return None

def resolve_sudoku_busca_largura(board):
    problema = SudokuBuscaEmLargura(board)
    solucao = Busca_em_largura(problema)
    return solucao.estado

def get_passos():
    global passos
    return passos