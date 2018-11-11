from classes_genetic import *
from obvious_solver import *
from copy import deepcopy
import random
import time

POPULATION_NUMBER = 1200
SURVIVAL_RATE = 0.35
MUTATION_RATE = 0.2
NUMBER_OF_CROSSOVER = 5
VERTICAL_SWITCHING_RATE = 0.4


def fitness(puzzle):
  complete_fields = 0
  for i in range(puzzle.size):
    horizontal_array = puzzle[i]
    vertical_array = getVertical(puzzle.puzzle_array, i)
    box_array = getBox(puzzle.puzzle_array, i)
    if len(set(vertical_array)) == 9: complete_fields += 1
    if len(set(box_array)) == 9: complete_fields +=1
    if len(set(horizontal_array)) == 9: complete_fields +=1
  return complete_fields

def giveBirth(parent_1, parent_2, crossover_points):
  child_1 = deepcopy(parent_1)
  child_2 = deepcopy(parent_2)

  genetic_engineering_functions = chooseDirection()
  for point in crossover_points:
    genetic_engineering_functions[0](child_1, child_2, point)

  # print("before")
  # print(child_1)
  # print(child_2)
  mutation(child_1, MUTATION_RATE, genetic_engineering_functions[1])
  mutation(child_2, MUTATION_RATE, genetic_engineering_functions[1])

  # print("after")
  # print(child_1)
  # print(child_2)
  return (child_1, child_2)

def crossHorizontal(child_1, child_2, point):
  save_horizontal = deepcopy(child_1[point])
  child_1.replaceHorizontal(child_2[point],point)
  child_2.replaceHorizontal(save_horizontal, point)
  
def crossVertical(child_1, child_2, point):
  save_vertical = deepcopy(child_1.puzzle_array[:,point])
  child_1.replaceVertical(child_2.puzzle_array[:,point], point)
  child_2.replaceVertical(save_vertical, point)

def mutation(puzzle, rate, createFunction):
  for i in range(puzzle.size):
    if random.random()< rate:
      createFunction(puzzle, i)

def createHorizontal(puzzle, number):
  available = set([i for i in range(1,10)])
  for taken in puzzle.fixed_hor[number]:
    available.discard(puzzle[number][taken])
  for j in range(puzzle.size):
    if j in puzzle.fixed_hor[number]: continue
    to_add = random.choice(tuple(available))
    available.discard(to_add)
    puzzle[number][j] = to_add

def createVertical(puzzle, number):
  available = set([i for i in range(1,10)])
  for taken in puzzle.fixed_ver[number]:
    available.discard(puzzle[taken][number])
  for i in range(puzzle.size):
    if i in puzzle.fixed_ver[number]: continue
    to_add = random.choice(tuple(available))
    available.discard(to_add)
    puzzle[i][number] = to_add

def chooseDirection():
  if random.random() < VERTICAL_SWITCHING_RATE:
    return (crossVertical, createVertical)
  return (crossHorizontal, createHorizontal)


def solveSudoku(puzzle):
  puzzle_processed = Puzzle(puzzle)
  puzzle_solved_obvious = solveObviousBoxes(puzzle_processed)
  print("Solved the obvious solutions")
  print(puzzle_solved_obvious)
  # time.sleep(2)
  population = dawnOfCivilization(puzzle_solved_obvious)
  greatestOfAllTime = evolution(population, 27)
  return greatestOfAllTime


def dawnOfCivilization(puzzle):
  population = []
  for i in range(POPULATION_NUMBER):
    organism = deepcopy(puzzle)
    for i in range(puzzle.size):
      createHorizontal(organism, i)
    population.append(organism)
  return population


def evolution(current_population, best_fit):
  population_evaluated = evaluatePopulation(current_population)
  (best_organism, fitting_value) = selectBestParent(population_evaluated)
  if fitting_value == best_fit: return best_organism
  print("Not there yet..")
  print("Fitting Value: {}".format(fitting_value))
  print(best_organism)
  next_generation = getNextGeneration(population_evaluated)
  return evolution(next_generation, best_fit)

def evaluatePopulation(population):
  evaluation = {}
  for organism in population:
    evaluation[organism] = fitness(organism)
  return evaluation
  
    
def getNextGeneration(population_dict):
  children = breedChildren(population_dict, ( 1 - SURVIVAL_RATE) * len(population_dict), [])
  surviving_parents = getSurvivors(population_dict, SURVIVAL_RATE * len(population_dict), [])
  return children + surviving_parents

def breedChildren(population_evaluated, population_target, children):
  if len(children) >= population_target:
    return children
  parent_1 = selectWeightedRandom(population_evaluated)
  parent_2 = selectWeightedRandom(population_evaluated)
  crossover_points = chooseCrossoverPoints(9, NUMBER_OF_CROSSOVER)
  babies = giveBirth(parent_1, parent_2, crossover_points)
  children.extend(babies)
  return breedChildren(population_evaluated, population_target, children)


def getSurvivors(population_dict, population_target, survivors):
  if len(survivors) >= population_target:
    return survivors
  (best_parent, value) = selectBestParent(population_dict)
  population_dict.pop(best_parent)
  survivors.append(best_parent)
  return getSurvivors(population_dict, population_target, survivors)

def chooseCrossoverPoints(number_range, number):
  crossover_points = []
  available_range = set([i for i in range(number_range)])
  for n in range(number):
    chosen_number = random.choice(tuple(available_range))
    crossover_points.append(chosen_number)
    available_range.discard(chosen_number)
  return crossover_points


def selectBestParent(choices):
  best_evaluation = 0
  best_parent = None
  for key, value in choices.items():
    if value > best_evaluation:
      best_parent = key
      best_evaluation = value
  return (best_parent, best_evaluation)

def selectWeightedRandom(choices):
  max = sum(choices.values())
  pick = random.uniform(0, max)
  current = 0
  for key, value in choices.items():
    current += value
    if current > pick:
      return key