from sudoku import Sudoku
# Initializes a Sudoku puzzle with 3 x 3 sub-grid and
# generates a puzzle with half of the cells empty
for i in range(10):
    puzzle = Sudoku(3).difficulty(0.9)
    print (puzzle, file=open("tests/inputs.txt", "a"))
