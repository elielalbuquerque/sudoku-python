import numpy, time
from generator.sudoku import Sudoku
from breadthFirstSearch.Sudoku_Player_BFS import SudokuPlayerBFS
from aStar.Sudoku_A_Star import SudokuPlayerAStar

#Gera 100 quadros com níveis de dificuldade do 0.1 (fácil, mais completo)
#até o 0.9 (mais dificil, menos completo)
def generate_inputs():
    for j in range (1, 10):
        print(f"Gerando inputs_{j}.txt.")
        file = open(f'tests/inputs/inputs_{j}.txt', 'w').close()
        for i in range (100):
            difficulty_graduation = float(f'0.{j}')
            board = Sudoku(3).difficulty(difficulty_graduation)
            print (board, file=open(f'tests/inputs/inputs_{j}.txt', "a"))


def solve_bfs(quadro,file_id):
    t1 = time.time()
    sudoku_bfs = SudokuPlayerBFS(quadro.tolist())
    result = numpy.asarray(sudoku_bfs.busca_em_largura(), dtype=numpy.int32)
    s = sudoku_bfs.get_steps()
    t = time.time() - t1
    print(f'{t} {s}',file=open(f"tests/results/bfs_{file_id}.txt", "a"))

def solve_A_star(quadro,file_id):
    t1 = time.time()
    sudoku_A_Star = SudokuPlayerAStar(quadro)
    result = numpy.asarray(sudoku_A_Star.solve_a_star(), dtype=numpy.int32)
    s = sudoku_A_Star.get_steps()
    t = time.time() - t1
    print(f'{t} {s}',file=open(f"tests/results/aStar_{file_id}.txt", "a"))


#Lê os quadros de entrada, resolve e joga os resultados em tests/results
def solve_inputs():
    for files_it in range (1,10):
        print (f'Calculating file {files_it}.')
        open(f'tests/results/aStar_{files_it}.txt', 'w').close()
        open(f'tests/results/bfs_{files_it}.txt', 'w').close()
        try:
            dados = open(f"tests/inputs/inputs_{files_it}.txt", "r")
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
                solve_bfs(quadro,files_it)
                #solve_A_star(quadro,files_it)
                contador = 0
                i = 0
                j = 0
                quadro = numpy.zeros((9,9))


#Função principal da aplicação.
def main():
    generate_inputs()
    solve_inputs()

if __name__ == "__main__":
    main()