import copy

#Classe que mantém o quadro de problemas
class SudokuStateBFS():
    def __init__(self, inicial):
        self.inicial = inicial
        self.tipo = len(inicial) # Define o tipo do quadro, 6x6 ou 9x9
        self.altura = int(self.tipo/3) # Define a altura dos quadrante (2 para 6x6, 3 para 9x9)

    # Retorna o cojunto de valores que não apacerem no quadro
    def filtra_valores(self, valores, usados):
        return [numero for numero in valores if numero not in usados]

    # Retorna o primeiro campo vazio marcado com 0
    def get_campo_vazio(self, quadro, estado):
        for linha in range(quadro):
            for coluna in range(quadro):
                if estado[linha][coluna] == 0:
                    return linha, coluna   

    def operacoes(self, estado):
        numeros_validos = range(1, self.tipo+1) # Define o conjunto de numeros válidos que podem ser colocados no quadr
        na_coluna = [] # Lista os valores válidos para serem inseridos nos campos vazios da coluna
        no_quadrante = [] # Lista os valores válidos para serem inseridos nos campos vazios do quadrante

        linha,coluna = self.get_campo_vazio(self.tipo, estado) # Pega o primro campo vazio no quadro

        # Filtra os valores validos baseado na linha
        na_linha = [numero for numero in estado[linha] if (numero != 0)]
        opcoes_validas = self.filtra_valores(numeros_validos, na_linha)

        # Filtra os valores validos baseado na coluna
        for column_index in range(self.tipo):
            if estado[column_index][coluna] != 0:
                na_coluna.append(estado[column_index][coluna])
        opcoes_validas = self.filtra_valores(opcoes_validas, na_coluna)

        # Filtra os valores validos baseado no quadrante
        linha_inicial = int(linha/self.altura)*self.altura
        coluna_inicial = int(coluna/3)*3
        
        for linha_quadrante in range(0, self.altura):
            for coluna_quadrante in range(0,3):
                no_quadrante.append(estado[linha_inicial + linha_quadrante][coluna_inicial + coluna_quadrante])
        opcoes_validas = self.filtra_valores(opcoes_validas, no_quadrante)

        for numero in opcoes_validas:
            yield numero, linha, coluna      

    # Retorna o quadro atualizado após adicionar um novo valor
    def resultado(self, state, operacao):

        jogo = operacao[0]
        linha = operacao[1]
        coluna = operacao[2]

        # Adiciona o novo valor ao quadro
        novo_estado = copy.deepcopy(state)
        novo_estado[linha][coluna] = jogo

        return novo_estado

    # Usa a soma de cada linha, coluna e quadrante para verificar a validade do quadro
    def testa_validade(self, state):

        # Soma esperada de cada linha, coluna ou quadrante.
        total = sum(range(1, self.tipo+1))

        # Checa linhas e colunas e retorna falso se o total não é valido
        for linha in range(self.tipo):
            if (len(state[linha]) != self.tipo) or (sum(state[linha]) != total):
                return False

            total_coluna = 0
            for coluna in range(self.tipo):
                total_coluna += state[coluna][linha]

            if (total_coluna != total):
                return False

        # Verifica os quadrantes e retorna falso se o total é inválido
        for coluna in range(0,self.tipo,3):
            for linha in range(0,self.tipo,self.altura):

                total_quadrante = 0
                for linha_quadrante in range(0,self.altura):
                    for coluna_quadrante in range(0,3):
                        total_quadrante += state[linha + linha_quadrante][coluna + coluna_quadrante]

                if (total_quadrante != total):
                    return False
        return True

    # Sobreescrita do metodo que transforma o objeto em string
    def __repr__(self):
        out_str = ''
        for i in range(9):
            if i in [3, 6]:
                out_str += '------+-------+------\n'
            line = ''
            for j in range(9):
                if j in [3, 6]:
                    line += '| '
                number = str(self.inicial[i][j]) if self.inicial[i][j] > 0 else '_'
                line += number + ' '
            out_str += line + '\n'
        return out_str