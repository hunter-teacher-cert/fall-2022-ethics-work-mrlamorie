import os
import time
import random


def makeMap(w=30, h=30, fill='.', dict=False, debug=False):
  '''
  A function to return a 2d array in the format of 
  @param w {int}: width of board
  @param h {int}: height of board
  @param fill {char}: default fill of board
  @param dict {bool}: dict(T) string(F)
  @param debug {bool}: if true, dict with name, x, y

  @return {list}: a 2d map
  '''
  
  # deal with option dict or text
  if dict:
    fill = {'name': fill}
  else:
    fill = fill

  # more verbose by design, gives studenta a location tool and
  # forces them to break out loops into a more classical form
  if debug:

    # make sure to deal with double true
    if dict:
      fill = fill.get('name')
      
    board = []
    for i in range(h):
      row = []
      for j in range(w):
        row.append({'name': fill, 'x': j, 'y': i})

      board.append(row)
    return board

  # pythonic way for simple board construction
  else:
    board = [[fill for i in range(h)] for j in range(w)]

  return board

def printMap(map, sep=' '): # split from makeMap later typically
  '''
  Prints a map from a 2d list of dicts, chars not supported. Char
  maps were for construction and understanding purposes only.
  @param map {list}: a 2d list of one of the required formats
  @param sep {char}: a seperator for each of the items
  '''
  for row in map:
    for col in row:
      print(col.get('name'), end=sep)
    print()
  print()

def coordPicker(n=115, w=30, h=30):
  '''
  Vomits out n number of sets of coordinates within the range
  of w for x and h for y. chose to do this with w and h rather than
  with the map, as it is used at seeding just like the map is
  @param n {int}: number of items to be vomited out.
  @param w {int}: number of columns
  @param h {int}: number of rows
  @return {list}: a list of coordinates in x & y format.
  '''
  coords = []
  # computationally heavy as the number of wanted items
  # approaches the size of the board, but very likely much like
  # a strong student answer
  while len(coords) < n:
    x = random.randrange(w)
    y = random.randrange(h)

    #check to see if they are unique coords
    unique = True
    for c in coords:
      if c.get('x') == x and c.get('y') == y:
        unique = False

    #it was unique
    if unique:
      coords.append({'x': x, 'y': y})

    
  return coords

def startBoard(w=30, h=30, p=100, c=15):
  
  return board
    
'''
step tests
print(makeMap(debug=True)) #makeMap tested
tst = makeMap(debug=True)
printMap(tst)  #printMap tested
print(coordPicker())
'''

