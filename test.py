import genetic_solver, tree_solver, classes
import unittest


puzzle_array_1 = [[5, 3, 4, 0, 7, 8, 9, 1, 2],
                  [6, 0, 2, 1, 9, 5, 3, 4, 8],
                  [1, 9, 8, 3, 4, 2, 5, 6, 7],
                  [8, 5, 9, 7, 0, 1, 4, 2, 3],
                  [4, 2, 6, 8, 5, 3, 7, 9, 1],
                  [7, 1, 0, 9, 2, 4, 8, 5, 6],
                  [9, 6, 1, 5, 3, 7, 2, 8, 4],
                  [2, 0, 7, 4, 1, 9, 6, 3, 5],
                  [3, 4, 5, 2, 8, 6, 1, 7, 0]]

puzzle_array_2 = [[3, 8, 0, 0, 1, 0, 6, 0, 2],
                  [0, 5, 1, 4, 0, 0, 0, 0, 0],
                  [0, 0, 6, 8, 0, 0, 0, 0, 1],
                  [0, 6, 9, 0, 0, 0, 0, 0, 8],
                  [0, 0, 5, 2, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 6, 2, 0, 0],
                  [0, 0, 0, 0, 3, 4, 0, 0, 0],
                  [0, 0, 0, 6, 5, 0, 0, 0, 0],
                  [0, 9, 0, 1, 0, 0, 5, 0, 0]]

puzzle_array_3 = [[0, 0, 0, 0, 1, 0, 8, 4, 0],
                  [0, 6, 0, 4, 0, 0, 0, 0, 0],
                  [0, 0, 0, 2, 0, 0, 6, 0, 7],
                  [1, 0, 4, 0, 2, 0, 0, 9, 3],
                  [0, 7, 0, 0, 3, 0, 0, 0, 2],
                  [8, 0, 0, 0, 0, 0, 0, 0, 0],
                  [4, 0, 0, 1, 0, 7, 0, 0, 0],
                  [0, 0, 0, 0, 4, 3, 0, 0, 0],
                  [0, 0, 6, 0, 0, 0, 1, 0, 0]]


class SudokuTest(unittest.TestCase):

  def _test_puzzleParse(self):
    puzzle = classes.Puzzle(puzzle_array_1)
    print(puzzle)
    return

  def _test_puzzleSolve(self):
    solved = genetic_solver.solveSudoku(puzzle_array_1)
    print(solved)
    return

  def test_puzzleSolveGuess(self):
    solved = genetic_solver.solveSudoku(puzzle_array_3)
    print(solved)



if __name__== '__main__':
  unittest.main()