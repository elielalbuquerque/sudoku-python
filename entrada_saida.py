import numpy

def convert_txt_to_array (arquivo):
    try:
        dados = open(arquivo, "r")
    except (FileNotFoundError, IOError):
        print("Arquivo de entrada não encontrado!")
    quadro = numpy.zeros((9,9))
    contador = 0
    i = 0
    j = 0
    eNumero = False
    while contador <81:
        conteudo=dados.readline()
        eNumero = False
        for x in range(len(conteudo)):
            try:
                if int(conteudo[x]) > 0 and int(conteudo[x]) < 10:
                    quadro[i,j]=int(conteudo[x])
                    j = j + 1
                    contador = contador +1
                    eNumero = True
            except ValueError:
                if conteudo[x]=='_':
                    j = j + 1
                    contador = contador +1
                    eNumero = True
                #else:
                    #print(content[x], 'is not regonized')
            if j == 9:
                j = 0
        if eNumero:
            i = i + 1
    return quadro   

def imprime_quadro(board):
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

def imprime_resultado(resultado, t, s=0):
    if resultado is None:
        print("Esse quadro não tem solução!")
    else:
        print(imprime_quadro(resultado))
        print(f'Tempo para resolução: {t} segundos!')
        print(f'Passos {s}!\n')
        arquivo_saida = 'saida.txt'
        try:
            numpy.savetxt(arquivo_saida, resultado, delimiter=' ', fmt='%d')
        except (FileNotFoundError, IOError):
            print("Arquivo de saída não encontrado!") 