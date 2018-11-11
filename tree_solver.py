from classes import *
from copy import deepcopy

def solve(puzzle):
  solveObviousBoxes(puzzle)
  if isSolved(puzzle): return puzzle
  iffy_boxes = getIffyBoxes(puzzle)
  while len(iffy_boxes):
    iffy_box, iffy_values = iffy_boxes.pop()
    for iffy_value in iffy_values:
      guess_puzzle = makeGuess(puzzle, iffy_box, iffy_value)
      if not solveObviousBoxes(guess_puzzle): continue
      if isSolved(guess_puzzle): return guess_puzzle
      solve(guess_puzzle)

def solveObviousBoxes(puzzle):
  box_to_solve, solve_values = getSolvableBox(puzzle)
  if not box_to_solve: return True
  if not solve_values: return False
  solveBox(puzzle, box_to_solve, solve_values.pop())
  solveObviousBoxes(puzzle)

def makeGuess(puzzle, guess_box, guess_value):
  new_puzzle = deepcopy(puzzle)
  solveBox(new_puzzle, guess_box, guess_value)
  return new_puzzle


def isSolved(puzzle):
  for box in puzzle.boxes:
    if box.val == 0 : 
      return False
  return True

def getSolvableBox(puzzle):
  """
  Tries to find a box that can already be filled with existing circumstances
  If box is found, return (box, [value_to_fill])
  If box is empty but there are no possible values, return (box, None)
  If no box with immediate solution is found, return (None, None)
  """
  for box in puzzle.boxes:
    if box.val: continue
    possible_values = getPossibleValues(puzzle, box)
    if len(possible_values) <= 1: return (box, possible_values)
  return None, None

def getIffyBoxes(puzzle):
  iffy_boxes = []
  for box in puzzle.boxes:
    if box.val: continue
    possible_values = getPossibleValues(puzzle, box)
    if len(possible_values) == 2: iffy_boxes.append((box, [i for i in possible_values]))
  return iffy_boxes      

def getPossibleValues(puzzle, box):
    possible_values = set([i for i in range(1,10)])
    taken_values_hor = set([other_box.val for other_box in puzzle.horizontal[box.i].boxes])
    taken_values_vert = set([other_box.val for other_box in puzzle.vertical[box.j].boxes])
    taken_values_box = set([other_box.val for other_box in puzzle.bigbox[puzzle.findBoxNumber(box.i, box.j)].boxes])
    possible_values = possible_values - taken_values_hor - taken_values_vert - taken_values_box
    return possible_values




def solveBox(puzzle, box, value):
  box.val = value
  puzzle.addBoxToCollections(box)  








# class Solver(object):
#   """docstring for Solver"""
#   def __init__(puzzle, puzzle):
#     super(Solver, puzzle).__init__()
#     puzzle.puzzle = puzzle
#     puzzle.box_stack = []

    
#   def solve_recurr(puzzle, was_guessing = False, tried=[]):
#     if checkGoal():
#       return puzzle.puzzle

#     box_to_fill, is_guessing = getBoxToFill(puzzle, tried)
#     guess = was_guessing or is_guessing

#     if box_to_fill:
#       box_stack.append(box_to_fill)
#       fillAction(box_to_fill)
#       solve_recurr(guess)

#     else:
#       wrong_box = box_stack.pop()
#       unfillAction(wrong_box)
#       tried.append(wrong_box)



#   def fillAction(puzzle, box, guess):
#     if not guess:
#       box.fixed = True
#     value = pop(box.possible)
#     puzzle.puzzle.removePossibleValueFromBoxes(box, value)
#     box.val = value

#   def unfillAction(puzzle, box, guess):
#     value = box.value
#     box.value = 0
#     puzzle.puzzle.addPossibleValueForBoxes(box, value)





#   def checkGoal(puzzle):
#     for box in puzzle.puzzle.boxes:
#       if not box.value:
#         return False
#     return True

#   def getBoxToFill(puzzle, tried):
#     min_possible = 9
#     min_possible_box = None
#     for box in puzzle.puzzle.boxes:
#       if box.value or box in tried:
#         continue
#       if not len(box.possible):
#         return False, False
#       if len(box.possible) == 1:
#         return box, False
#       if len(box.possible) < min_possible:
#         min_possible = len(box.possible)
#         min_possible_box = box
#     return min_possible_box, True

    
    