

def solveObviousBoxes(puzzle):
  coordinates, solve_value = getSolvableBox(puzzle)
  if not coordinates: return puzzle
  (i, j) = coordinates
  puzzle[i][j] = solve_value
  puzzle.updateFixed(i, j)
  return solveObviousBoxes(puzzle)

def getSolvableBox(puzzle):
  """
  Tries to find a box that can already be filled with existing circumstances
  If box is found, return (box, [value_to_fill])
  If box is empty but there are no possible values, return (box, None)
  If no box with immediate solution is found, return (None, None)
  """
  for i in range(puzzle.size):
    for j in range(puzzle.size):
      if puzzle[i][j]: continue
      possible_values = getPossibleValues(puzzle, i, j, findBoxNumber(i, j))

      if len(possible_values) == 1: 
        print("coords: {} possible: {}".format((i, j), possible_values))

        return ((i,j),possible_values.pop())
  return None, None



def findBoxNumber(i, j):
  return 3 * (i//3) + (j//3)


def getVertical(puzzle_array, number):
  return puzzle_array[ :, number]

def getBox(puzzle_array, number):
  start_i = number // 3 * 3
  start_j = number % 3 * 3
  matrixOfValues = puzzle_array[start_i: start_i + 3, start_j : start_j + 3]
  listofValues = []
  for value in matrixOfValues.flat:
    listofValues.append(value)
  return listofValues


def getPossibleValues(puzzle, hor_number, vert_number, box_number):
    possible_values = set([i for i in range(1,10)])
    taken_values_hor = set(puzzle[hor_number])
    taken_values_vert = set(getVertical(puzzle, vert_number))
    taken_values_box = set(getBox(puzzle, box_number))
    possible_values = possible_values - taken_values_hor - taken_values_vert - taken_values_box
    return possible_values




def solveBox(puzzle, box, value):
  box.val = value
  puzzle.addBoxToCollections(box)  




    