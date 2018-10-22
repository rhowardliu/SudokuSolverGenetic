from classes import *

class Solver(object):
  """docstring for Solver"""
  def __init__(self, puzzle):
    super(Solver, self).__init__()
    self.puzzle = puzzle
    self.box_stack = []

    
  def solve_recurr(self, was_guessing = False, tried=[]):
    if checkGoal():
      return self.puzzle

    box_to_fill, is_guessing = getBoxToFill(puzzle, tried)
    guess = was_guessing or is_guessing

    if box_to_fill:
      box_stack.append(box_to_fill)
      fillAction(box_to_fill)
      solve_recurr(guess)

    else:
      wrong_box = box_stack.pop()
      unfillAction(wrong_box)
      tried.append(wrong_box)



  def fillAction(self, box, guess):
    if not guess:
      box.fixed = True
    value = pop(box.possible)
    self.puzzle.removePossibleValueFromBoxes(box, value)
    box.val = value

  def unfillAction(self, box, guess):
    value = box.value
    box.value = 0
    self.puzzle.addPossibleValueForBoxes(box, value)





  def checkGoal(self):
    for box in self.puzzle.boxes:
      if not box.value:
        return False
    return True

  def getBoxToFill(self, tried):
    min_possible = 9
    min_possible_box = None
    for box in self.puzzle.boxes:
      if box.value or box in tried:
        continue
      if not len(box.possible):
        return False, False
      if len(box.possible) == 1:
        return box, False
      if len(box.possible) < min_possible:
        min_possible = len(box.possible)
        min_possible_box = box
    return min_possible_box, True

    
    