from obvious_solver import *

GUESS_RANGE = 2


def fillObvious(puzzle, pos = (0, 0), guessable = []):
  (i, j) = pos
  if not puzzle[i][j]:
    possible_values = getPossibleValues(puzzle, (i, j))
    if len(possible_values) == 1:
      puzzle[i][j] = possible_values.pop()
      print(puzzle)
      print('')
      return fillObvious(puzzle, guessable = [])
    elif len(possible_values) <= GUESS_RANGE:
      guessable.append((i, j))
  next_pos = nextPos(pos)  
  if not next_pos:
    return guessable
  return fillObvious(puzzle, next_pos, guessable)




def solve(puzzle, guessable = []):
  if not guessable:
    guessable = fillObvious(puzzle)
  if checkSolved(puzzle):
    return puzzle
  box_to_guess = guessable.pop()
  (i, j) = box_to_guess
  available_guesses = getPossibleValues(puzzle, box_to_guess)
  for num in available_guesses:
    print('{}, {}:'.format(i, j))
    print(num)
    puzzle[i][j] = num
    guessIsOkay = fillGuess(puzzle, (0,0), box_to_guess, {})
    print(puzzle)
    if guessIsOkay:
      return solve(puzzle, guessable)


def fillGuess(puzzle, pos, asserted_by, asserted_dic):
  asserted_dic[pos] = asserted_by
  (i, j) = pos
  if not puzzle[i][j]:
    possible_values = getPossibleValues(puzzle, (i, j))
    if len(possible_values) == 0:
      return retract(puzzle, pos, asserted_dic)
    if len(possible_values) == 1:
      puzzle[i][j] = possible_values.pop()
      print('filled guess')
      print(puzzle)
      return fillGuess(puzzle, (0,0), pos, asserted_dic)
  next_pos = nextPos(pos)
  if not next_pos:
    return True
  return fillGuess(puzzle, next_pos, asserted_by, asserted_dic)



def checkSolved(puzzle):
  for i in range(len(puzzle[0])):
    for j in range(len(puzzle[0])):
      if not puzzle[i][j]: return False
  return True

def retract(puzzle, pos, asserted_dic):
  if len(asserted_dic) == 0:
    return False
  (i, j) = pos
  print('retracting', pos)
  puzzle[i][j] = 0
  if pos in asserted_dic.keys():
    asserted_pos = asserted_dic.pop(pos)
    return retract(puzzle, asserted_pos, asserted_dic)
