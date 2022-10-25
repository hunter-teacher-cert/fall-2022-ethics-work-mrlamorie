import os
import time
import random
import copy

## -------- map making f(x)ns

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


## -------- coord f(x)ns

def posMoves(x, y, w, h, teleport):
  '''
  posMoves
  returns a set of moves on the board within the params of the board
  and if teleport = true or !
  This could have been written with a dict pass and the map edges,
  but this generic version allows for easier testing and should
  be simular under the hood
  @param {int} x : x value to be tested
  @param {int} y : y value to be tested
  @param {int} w : max width value
  @param {int} h : max height value
  @param {bool} teleport : true or false can teleport

  @return {list}: a list of coordiantes in x y keyed dictionary
  '''
  moves = [] # for the potential moves

  #long and explicit way - likely what students will pick
  x1 = x -1
  if x1 < 0:
    x1 = x1 + w
  if abs(x - x1) == 1:
    moves.append({'x': x1, 'y': y})
  if (abs(x - x1) != 1) and teleport == True: #constraint
    moves.append({'x': x1, 'y': y})
    
  x1 = x + 1
  if x1 == w:
    x1 = 0
  if abs(x - x1) == 1:
    moves.append({'x': x1, 'y': y})
  if (abs(x - x1) != 1) and teleport == True: #constraint
    moves.append({'x': x1, 'y': y})
  
  y1 = y -1
  if y1 < 0:
    y1 = y1 + h
  if abs(y - y1) == 1:
    moves.append({'x': x, 'y': y1})
  if (abs(y - y1) != 1) and teleport == True: #constraint
    moves.append({'x': x, 'y': y1})  
  
  y1 = y + 1
  if y1 == h:
    y1 = 0
  if abs(y - y1) == 1:
    moves.append({'x': x, 'y': y1})
  if (abs(x - x1) != 1) and teleport == True: #constraint
    moves.append({'x': x, 'y': y1})

  random.shuffle(moves) #because random walk
  return moves


def move(x, y, w, h, fill, map):
  '''
  Moves the player. Updates age, and updates hunger. If the player 
  has more then one move in their list all moves other then the last one
  will be considered attempts to eat.
  @param {int} x : x value to be tested
  @param {int} y : y value to be tested
  @param {int} w : max width value
  @param {int} h : max height value
  @param {char} fill : default fill of map
  @param {list} map : the gameplay map

  @return none
  '''
  local = posMoves(x, y, w, h, map[y][x]['teleport'])
  
  map[y][x]['age'] += 1 #age up the critter
  if map[y][x]['maxHunger'] != -1:
    map[y][x]['hunger'] += 1 #make hungry if needbe

  moved = False

  for type in map[y][x]['order']:
    for loc in local:
      if moved == False: #to cut down on extra loops 
        # the below works because it will eat anything other
        # than the fill because fill is noted in the list
        # as 'empty'
        if map[loc['y']][loc['x']]['name'] == type:
          
          if map[y][x]['hunger'] > 0 and type != fill:
            map[y][x]['hunger'] = 0
            
          map[loc['y']][loc['x']] = copy.deepcopy(map[y][x])
          map[y][x] = {'name' : fill}
          moved = True
          
  

## -------- game f(x)ns

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
      map[coord.get('y')][coord.get('x')] = copy.deepcopy(i.get('stats'))
      placed += 1
    
  
  return map

'''
test player dictionaries - 
prey =  {'number': 100, 'stats' : {'name': 'O', 'age': 0, 'maxAge': 3, 'hunger': -1, 'maxHunger': -1, 'teleport': True, 'order':  ['empty'] } }

predator =  {'number': 15, 'stats' : {'name': 'X', 'age': 0, 'maxAge': 6, 'hunger': 0, 'maxHunger': 3, 'teleport': True, 'order':  ['O', 'empty'] } }

'''

tst = makeMap(w=10, h=10, fill='.', dict=True, debug=False)

tst[0][0] = {'name': 'X', 'age': 0, 'maxAge': 6, 'hunger': 0, 'maxHunger': 3, 'teleport': False, 'order':  ['O', '.'] }

tst[0][1] = {'name': 'O', 'age': 0, 'maxAge': 3, 'hunger': -1, 'maxHunger': -1, 'teleport': True, 'order':  ['empty'] }
#print(posMoves(0, 0, 10, 10, False))
move(0, 0, 10, 10, '.', tst)

printMap(tst)
print(tst[0][1])

