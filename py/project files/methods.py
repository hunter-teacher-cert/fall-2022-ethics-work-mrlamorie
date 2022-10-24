import os
import time
import random
import copy


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

  #simple pythonic construction
  if not dict and not debug:
    board = [[fill for i in range(h)] for j in range(w)]
    return board
    
  if debug:
    # make sure to deal with double true
      
    board = []
    for i in range(h):
      row = []
      for j in range(w):
        row.append({'name': fill, 'x': j, 'y': i})

      board.append(row)
    return board


  else:
    board = [[{'name': fill} for i in range(h)] for j in range(w)]

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

def startBoard(w, h, *players):
  '''
  makes a board with a width of w, height of h, and players of each type and number of type. Players are defined by a proto like dictionary. EG - 
  predator = {'number': 15, info: {'name': 'X', 'age': 0, 'maxAge': 6, 'hunger': 0, 'maxHunger': 3, 'teleport': False, 'order':  
 ['O', '.']}}
prey =  {'number': 100, info:{'name': 'O', 'age': 0, 'maxAge': 3, 'hunger': -1, 'maxHunger': -1, 'teleport': True, 'order':  
 ['.']}}
  @param w {int}: the width of the map
  @param h {int}: the height of the map
  @param *players {dict}: the players and their rules as above

  @return {list}: a 2d board populated with players
  '''
  #get total number of players
  totalPlayers = 0
  for i in players:
    totalPlayers += i.get('number')

  #make sure total number of players !> board size
  if totalPlayers > (w * h):
    raise Exception("Can not have more players then board size")

  #otherwise, get spaces make map, combine
  placementList = coordPicker(totalPlayers, w, h)
  map = makeMap(w, h, fill='.', dict=True)

  #have map & coords, do the 
  for i in players:
    placed = 0 #track how many have been placed
    while placed < i.get('number'):
      coord = placementList.pop()
      print(coord)
      map[coord.get('y')][coord.get('x')] = 'insert deep copy here'
      placed += 1
    
  
  return map
'''
test player dictionaries - 
predator = {'number': 15, {'name': 'X', 'age': 0, 'maxAge': 6, 'hunger': 0, 'maxHunger': 3, 'teleport': False, 'order':  
 ['O', '.']}}
prey =  {'number': 100, {'name': 'O', 'age': 0, 'maxAge': 3, 'hunger': -1, 'maxHunger': -1, 'teleport': True, 'order':  
 ['.']}}
step tests
print(makeMap(debug=True)) #makeMap tested
tst = makeMap(debug=True)
printMap(tst)  #printMap tested
print(coordPicker())
tst = startBoard(-1, -1, {'number': 30}, {'number': 15}, {'number': 10})
print(tst) #startBoard *args tested, range error tested
'''





prey =  {'number': 5, 'stats:' : {'name': 'O', 'age': 0, 'maxAge': 3, 'hunger': -1, 'maxHunger': -1, 'teleport': True, 'order':  ['.'] } }

predator =  {'number': 15, 'stats' : {'name': 'O', 'age': 0, 'maxAge': 6, 'hunger': 0, 'maxHunger': 3, 'teleport': True, 'order':  ['O', '.'] } }

tst = startBoard(30, 30, prey, predator)

printMap(tst)
