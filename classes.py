class Box(object):
  """docstring for Box"""
  def __init__(self, i, j, val=0, fixed = False):
    super(Box, self).__init__()
    self.i = i
    self.j = j
    self.val = val
    self.fixed = fixed

class BoxCollection(object):
  """docstring for BoxCollection"""
  def __init__(self):
    super(BoxCollection, self.boxes).__init__()
    self.boxes = []

  def __getitem__(self, key):
    return (self.boxes[key]) if (self.boxes and key in self.boxes) else None    

  def addCollection(self, box):
    self.boxes.append(box)


class Puzzle(object):
  """docstring for Puzzle"""
  def __init__(self, puzzle_array):
    super(Puzzle, self).__init__()
    self.puzzle_array = puzzle_array
    self.boxes = []
    self.unsolvedBoxes = []
    for i, j in puzzle_array:    
      box_value = puzzle_array[i][j]
      newBox = Box(i, j, val=box_value, fixed = True, possible=[]) if box_value else Box(i, j)
      self.boxes.append(newBox)
      self.unsolvedBoxes.append(newBox) if not box_value
    self.horizontal = [BoxCollection() for i in range(9)]
    self.vertical = [BoxCollection() for i in range(9)]
    self.bigbox = [BoxCollection() for i in range(9)]
    self.initCollections()

  def initCollections(self):
    for box in self.boxes:
      if not box.val: continue
      self.addBoxToCollections(box)

  def addBoxToCollections(self, box):
    self.horizontal[box.i].addCollection(box)
    self.vertical[box.j].addCollection(box)
    self.bigbox[findBoxNumber(box.i, box.j)].addCollection(box)

  def findBoxNumber(self, i, j)
    return 3* (j//3) + (i//3)