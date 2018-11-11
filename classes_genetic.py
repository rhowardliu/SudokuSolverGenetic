import numpy as np


class Puzzle(object):
  """docstring for Puzzle"""
  def __init__(self, puzzle):
    super(Puzzle, self).__init__()
    self.puzzle_array = np.array(puzzle)
    self.size = len(puzzle[0])
    self.fixed_hor = {}
    self.fixed_ver = {}
    self.addListtoDict(self.fixed_hor)
    self.addListtoDict(self.fixed_ver)    
    for i in range(self.size):
      for j in range(self.size):
        if self.puzzle_array[i][j]: 
          self.updateFixed(i, j)
          
  def updateFixed(self,i, j):
    self.fixed_hor[i].append(j)
    self.fixed_ver[j].append(i)

  
  def addListtoDict(self, my_dict):
    for i in range(self.size):
      my_dict[i] = []

  def __getitem__(self, index):
    return self.puzzle_array[index]

  def replaceHorizontal(self,horizontal, number):
    self.puzzle_array[number] = horizontal

  def replaceVertical(self, vertical, number):
    for i in range(len(vertical)):
      self.puzzle_array[i][number] = vertical[i]

  def __str__(self):
    return str(self.puzzle_array)