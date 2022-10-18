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

def coorPicker(n=115, w=30, h=30):
  return ({'x':0, 'y':0})

def populateBoard(board, h=100, n=15):
  return ()
    
'''
step tests
print(makeMap(debug=True)) #makeMap tested
tst = makeMap(debug=True)
printMap(tst)  #printMap tested
'''

