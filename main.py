import time

import numpy as np

import solver

import file_to_array as converter

def main():
    f = open("imput.txt", "r")
    board = np.zeros((9,9))
    board = converter.covert_txt_to_array(f)
    print('Board loaded')
    print(board)

    b = solver.SudokuSolver(board)

    t1 = time.time()

    b.solve()

    t2 = time.time() - t1

    assert b.valid_board()

    print(f"Time: {t2} seconds")
    print(f"Steps: {b.num_steps}")
    print('Board resolved')
    print(b.board)

if __name__ == "__main__":
    main()