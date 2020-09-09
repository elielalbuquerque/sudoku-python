# sudoku-python

This working is part of Programming Techniques discipline in Unisinos's Computer Science postgraduate program. Here you can find two sudoku solvers aproaches, firstly a implementation of [Breadth-first Search](https://en.wikipedia.org/wiki/Breadth-first_search). Second is used a implementation based on [A* Search Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm).
 A simple python console application that reads an input sudoku from [input.txt](input.txt) and solves it using above algorithms.

 # User Instructions
 ## Basic Utilization
 ### Input Board to Solve

 First insert the board to solve in the file [input.txt](input.txt) in format like this:

5 3 _ | _ 7 _ | _ _ _<br />
6 _ _ | 1 9 5 | _ _ _<br />
_ 9 8 | _ _ _ | _ 6 _<br />
------+-------+------<br />
8 _ _ | _ 6 _ | _ _ 3<br />
4 _ _ | 8 _ 3 | _ _ 1<br />
7 _ _ | _ 2 _ | _ _ 6<br />
------+-------+------<br />
_ 6 _ | _ _ _ | 2 8 _<br />
_ _ _ | 4 1 9 | _ _ 5<br />
_ _ _ | _ 8 _ | _ 7 9<br />

Before insert confirm if this is a valid sudoku board.

Second step is to run the [main.py](main.py) and select the algorithm to solve the board. Chose one of four options, 1 resolve using BFS, 2 resolve using aStar, 3 resolve using both and 4 exit of program.

 ## Extra Options
 ### Test Solving Algorithms

For testing performance of both algorithms we use [py-sudoku project](https://pypi.org/project/py-sudoku/). We imported this project to our code, in [sudoku.py](generator/sudoku.py) to edit de print method with objective to facilitate the coversion of sudoku board to array.

For generate the tests boards and calculate yours outpus run [tests.py]. 
 

# Prerequisites
  * Python 3

# Author
Gustavo Zanatta Bruno @zanattabruno
Guilherme Falcão Silva Campos @guilhermefscampos