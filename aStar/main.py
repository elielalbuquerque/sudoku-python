from Sudoku_A_Star import SudokuPlayerAStar, SudokuStateAStar


def parser(input_string):
    grid = []
    for row in input_string.splitlines():
        row = row.strip()
        if not row.startswith('-') and row != '':
            row = row.replace(' ', '').replace('_', '0').replace('|', '')
            int_row = [int(value) for value in row]
            grid.append(int_row)
    return grid


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_string = """
    5 3 _ | _ 7 _ | _ _ _
    6 _ _ | 1 9 5 | _ _ _
    _ 9 8 | _ _ _ | _ 6 _
    ------+-------+------
    8 _ _ | _ 6 _ | _ _ 3
    4 _ _ | 8 _ 3 | _ _ 1
    7 _ _ | _ 2 _ | _ _ 6
    ------+-------+------
    _ 6 _ | _ _ _ | 2 8 _
    _ _ _ | 4 1 9 | _ _ 5
    _ _ _ | _ 8 _ | _ 7 9
    """

    board = parser(input_string)

    sudoku = SudokuPlayerAStar(board)
    print("Estado inicial")
    print(sudoku)
    print("Solução final")
    sudoku.solve_a_star()

