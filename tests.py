import numpy, time
from sudoku import Sudoku
from breadthFirstSearch.Sudoku_Player_BFS import SudokuPlayerBFS
from aStar.Sudoku_A_Star import SudokuPlayerAStar


def generate_inputs():
    for i in range(100):
        for j in range (1, 10):
            difficulty_graduation = float(f'0.{j}')
            board = Sudoku(3).difficulty(difficulty_graduation)
            with open(f'tests/inputs_{j}.txt','w'):
                pass
            print (board, file=open(f'tests/inputs_{j}.txt', "a"))

def solve_inputs():
    for files_it in range (1,10):
        print (f'Calculating file {files_it}')
        try:
            dados = open(f"tests/inputs_{files_it}.txt", "r")
        except (FileNotFoundError, IOError):
            print("Arquivo de entrada não encontrado!")
        quadro = numpy.zeros((9,9))
        contador = 0
        i = 0
        j = 0
        eNumeroLinha = False
        line_valid_places=[2,4,6,10,12,14,18,20,22]
        for conteudo in dados:
            eNumeroLinha = False
            for x in range(len(conteudo)):
                try:
                    if int(conteudo[x]) > 0 and int(conteudo[x]) < 10:
                        quadro[i,j]=int(conteudo[x])
                        j = j + 1
                        contador = contador +1
                        eNumeroLinha = True
                except ValueError:
                    if (x in line_valid_places) and (conteudo[0])=='|':
                        j = j + 1
                        contador = contador +1
                        eNumeroLinha = True
                    #else:
                        #print(conteudo[x], 'is not regonized')
                if j == 9:
                    j = 0    
            if eNumeroLinha:
                i = i + 1
                eNumeroLinha = False
            if i == 9:
                print(quadro)
                t1 = time.time()
                sudoku_bfs = SudokuPlayerBFS(quadro.tolist())
                result = numpy.asarray(sudoku_bfs.busca_em_largura(), dtype=numpy.int32)
                s = sudoku_bfs.get_steps()
                t = time.time() - t1
                print(f'{t} {s}',file=open(f"tests/bfs_{files_it}.txt", "a"))
                contador = 0
                i = 0
                j = 0
                quadro = numpy.zeros((9,9))
       

#solve_inputs()
