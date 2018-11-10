from classes import *


def solve_recur(puzzle, to_guess = True):
  solveObviousBoxes(puzzle)
  if isSolved(puzzle): return puzzle
  if to_guess:
    iffy_boxes = getIffyBoxes(puzzle)
    while len(iffy_boxes):
      iffy_box, iffy_values = iffy_boxes.pop()

def solveObviousBoxes(puzzle):
  box_to_solve, solve_value = getSolvableBox(puzzle)
  if not box_to_solve:
    return
  solveBox(puzzle, box_to_solve, solve_value)
  solveObviousBoxes(puzzle)


def isSolved(puzzle):
for box in puzzle.boxes:
  if box.val == 0 : return False
return True

def getSolvableBox(puzzle):
  for box in boxes:
    if box.val: continue
    possible_values = [i for i in range(1,10)]
    possible_values.remove(box.val for box in puzzle.horizontal[box.i].boxes)
    possible_values.remove(box.val for box in puzzle.vertical[box.j].boxes)
    possible_values.remove(box.val for box in puzzle.bigbox[findBoxNumber(box.i, box.j)].boxes)
    if len(possible_values) == 1: return (box, possible_values.pop())
  return None

def getIffyBoxes(puzzle):
  iffy_boxes = []
  for box in boxes:
    if box.val: continue
    possible_values = [i for i in range(1,10)]
    possible_values.remove(box.val for box in puzzle.horizontal[box.i].boxes)
    possible_values.remove(box.val for box in puzzle.vertical[box.j].boxes)
    possible_values.remove(box.val for box in puzzle.bigbox[findBoxNumber(box.i, box.j)].boxes)
    if len(possible_values) == 2: iffy_boxes.append((box, [i for i in possible_values]))
  return iffy_boxes      


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

    
    