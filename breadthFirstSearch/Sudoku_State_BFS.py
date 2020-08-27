import copy

#Classe que mantém o quadro de problemas
class SudokuStateBFS():
    def __init__(self, start):
        self.start = start
        self.type = len(start) # Define o tipo do quadro, 6x6 ou 9x9
        self.height = int(self.type/3) # Define a altura dos quadrante (2 para 6x6, 3 para 9x9)

    # Retorna o cojunto de valores que não apacerem no quadro
    def filter_values(self, values, useds):
        return [number for number in values if number not in useds]

    # Retorna o primeiro campo vazio marcado com 0
    def get_empty_field(self, board, state):
        for line in range(board):
            for column in range(board):
                if state[line][column] == 0:
                    return line, column   

    def operations(self, state):
        valis_numbers = range(1, self.type+1) # Define o conjunto de numeros válidos que podem ser colocados no quadr
        in_column = [] # Lista os valores válidos para serem inseridos nos campos vazios da coluna
        in_quadrant = [] # Lista os valores válidos para serem inseridos nos campos vazios do quadrante

        line,column = self.get_empty_field(self.type, state) # Pega o primro campo vazio no quadro

        # Filtra os valores validos baseado na linha
        in_line = [number for number in state[line] if (number != 0)]
        valid_operations = self.filter_values(valis_numbers, in_line)

        # Filtra os valores validos baseado na coluna
        for column_index in range(self.type):
            if state[column_index][column] != 0:
                in_column.append(state[column_index][column])
        valid_operations = self.filter_values(valid_operations, in_column)

        # Filtra os valores validos baseado no quadrante
        initial_line = int(line/self.height)*self.height
        initial_column = int(column/3)*3
        
        for line_quadrant in range(0, self.height):
            for column_quadrant in range(0,3):
                in_quadrant.append(state[initial_line + line_quadrant][initial_column + column_quadrant])
        valid_operations = self.filter_values(valid_operations, in_quadrant)

        for number in valid_operations:
            yield number, line, column      

    # Retorna o quadro atualizado após adicionar um novo valor
    def result(self, state, operation):

        game = operation[0]
        line = operation[1]
        column = operation[2]

        # Adiciona o novo valor ao quadro
        new_state = copy.deepcopy(state)
        new_state[line][column] = game

        return new_state

    # Usa a soma de cada linha, coluna e quadrante para verificar a validade do quadro
    def test_validity(self, state):

        # Soma esperada de cada linha, coluna ou quadrante.
        total = sum(range(1, self.type+1))

        # Checa linhas e colunas e retorna falso se o total não é valido
        for line in range(self.type):
            if (len(state[line]) != self.type) or (sum(state[line]) != total):
                return False

            total_column = 0
            for column in range(self.type):
                total_column += state[column][line]

            if (total_column != total):
                return False

        # Verifica os quadrantes e retorna falso se o total é inválido
        for column in range(0,self.type,3):
            for line in range(0,self.type,self.height):

                total_quadrant = 0
                for line_quadrant in range(0,self.height):
                    for coluna_quadrante in range(0,3):
                        total_quadrant += state[line + line_quadrant][column + coluna_quadrante]

                if (total_quadrant != total):
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
                number = str(self.start[i][j]) if self.start[i][j] > 0 else '_'
                line += number + ' '
            out_str += line + '\n'
        return out_str