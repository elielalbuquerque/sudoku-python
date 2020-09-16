import numpy

def convert_txt_to_array (file):
    try:
        datas = open(file, "r")
    except (FileNotFoundError, IOError):
        print("Arquivo de entrada não encontrado!")
    board = numpy.zeros((9,9))
    counter = 0
    i = 0
    j = 0
    is_number = False
    while counter <81:
        content=datas.readline()
        is_number = False
        for x in range(len(content)):
            try:
                if int(content[x]) > 0 and int(content[x]) < 10:
                    board[i,j]=int(content[x])
                    j = j + 1
                    counter = counter +1
                    is_number = True
            except ValueError:
                if content[x]=='_':
                    j = j + 1
                    counter = counter +1
                    is_number = True
                #else:
                    #print(content[x], 'is not regonized')
            if j == 9:
                j = 0
        if is_number:
            i = i + 1
    return board   

def print_board(board):
    out_str = ''
    for i in range(9):
        if i in [3, 6]:
            out_str += '------+-------+------\n'
        line = ''
        for j in range(9):
            if j in [3, 6]:
                line += '| '
            number = str(board[i][j]) if board[i][j] > 0 else '_'
            line += number + ' '
        out_str += line + '\n'
    return out_str

def print_result(result, t, s=0):
    if result is None:
        print("Esse quadro não tem solução!")
    else:
        print(print_board(result))
        print(f'Tempo para resolução: {t} segundos!')
        print(f'Passos {s}!\n')
        arquivo_saida = 'output.txt'
        try:
            numpy.savetxt(arquivo_saida, result, delimiter=' ', fmt='%d')
        except (FileNotFoundError, IOError):
            print("Arquivo de saída não encontrado!") 