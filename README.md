# sudoku-python

This working is part of Programming Techniques discipline in Unisinos 's Computer Science postgraduate program. Here you can find two sudoku solvers approaches, firstly a implementation of [Breadth-first Search](https://en.wikipedia.org/wiki/Breadth-first_search). Second is used a implementation based on [A* Search Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm).
 A simple python console application that reads an input sudoku from [input.txt](input.txt) and solves it using above algorithms.

 ## User Instructions
 ### Basic Utilization
 #### Input Board to Solve

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

 ### Extra Options
 #### Test Solving Algorithms

For testing performance of both algorithms we use [py-sudoku project](https://pypi.org/project/py-sudoku/). We imported this project to our code, in [sudoku.py](generator/sudoku.py,) to edit print method with objective to facilitate the conversion of sudoku board to array. With this package we implement our code to generate five files each containing 100 randomly generated frames, first one file with 10% of blanc spaces, next one with 20% up until 50 % the blanc spaces (more complexity).
Observation: with complexity bigger than 50% of blanc spaces  our implementation of aStar algorithm entry in loop.

For generate the tests boards and calculate yours outputs run [tests.py](tests.py). When run generated boards will be allocated in path [inputs](tests/inputs/). The results of the tests will be allocated in
path [results](tests/results/). The results are composed by number of steps and time for resolution for each algorithm.

 #### Analysis of algorithms
To execute analysis of both algorithms run [data_analysis.py](data_analysis.py), he's calculate the median steps and time to solve boards for each difficult level (10% until 50% of blanc spaces in boards), the output of these calculations are in [tests](tests/) folder, one to aStar e one to BFS.
First row is to difficult level min, in other words 10 % of blanc spaces, second row to 20% and so on, until 50 %. First data in each row are median execution time for this difficulty level, second median steps, third  max number of steps, fourth min number of steps, fifth max execution time and sixth min execution time.
After all calculations are plotted several pictures to provide a best analysis of the algorithms performance.

## Prerequisites
  * Python 3
  * Package numpy

## Authors
Gustavo Zanatta Bruno @zanattabruno
Guilherme Falcão Silva Campos @guilhermefscampos