# gol.py
# William LaMorie
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

import os
import time

"""
/**
   The Rules of Life:

   Survivals:
   * A living cell with 2 or 3 living neighbours will survive for the next generation.

   Deaths:
   * Each cell with >3 neighbours will die from overpopulation.
   * Every cell with <2 neighbours will die from isolation.

   Births:
   * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.

   NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.
*/
"""

def newBoard(rows, cols, sym='.'):#tested & works
  """a function to make a new board filled with symbol sym of row x col size """
  # need to use the more verbose method below because of shallow list in python
  board = [[sym for i in range(cols)] for j in range(rows)]
  return board
  
def printBoard(board):
  """A function to print a 2d array (board) as a grid"""
  for r in board:
    for c in r:
      print(c, end=' ') #end =' ' doube duties not adding a NL & spacing out
    print()

def setCell(board, cord, sym):
  """A function that takes in 2d array "board" and sets the string value of a
  cell at board[coordinates] to symbol sym. """

  board[cord[0]][cord[1]] = sym


def validNeighbors(board, cord):
  """A function that takes a location of cord on a board, uses the board's
  size at row 0 (assumes a non jagged board) to return a list of touples of 
  neighbors that are valdily within the correct area of the board."""
  
  maxRow = len(board) -1
  maxCol = len(board[0]) -1
  goodCords = []

  #small than going though the whole thing
  for i in range(-1, 2):
    for j in range(-1, 2):
      testCord = (cord[0] + i, cord[1] + j)

      #ugly conditional
      if (testCord[0] >= 0 and testCord[0] <= maxRow 
          and testCord[1] >= 0 and testCord[1] <= maxCol):
            
        #second ugly conditional
        if not(cord[0] == testCord[0] and cord[1] == testCord[1]):
          goodCords.append(testCord) #on the board and not self

  return goodCords
        
def countNeighbors(board, cord, sym="X"):
  """A function to count the number of living neighbors with the valid neighbors
  of a given coord, a living neigbor as defined by symol sym"""

  testCells = validNeighbors(board,cord)  #get list of valid cells as tuples 
  living = 0 # number of living neighbors
  
  for cell in testCells:
    if board[cell[0]][cell[1]] == sym:
      living += 1

  return living

def ageCell(board, cord, sym="X", alt= "."):
  """A function that checks what the cel value will update to based on the
  rules outlined for cgol, returns sym if alive, alt if not"""
    
  friends = countNeighbors(board, cord, sym) ## how many buddies
  living = board[cord[0]][cord[1]] == sym
  
  if living and friends == 2:
    return sym
  elif friends == 3:
    return sym
  else:
    return alt
    
    
def ageBoard(board, sym="X", alt="."):
  nextGen =  newBoard(len(board), len(board[0]))

  for i in range(len(board)):
    for j in range(len(board[0])):
      nextGen[i][j] = ageCell(board, (i, j), sym, alt)

  return nextGen
    
  
### test 1 - block &  blinker
  
tst = newBoard(10,10)
## 3 -> block
setCell(tst, (1,1), "X")
setCell(tst, (1,2), "X")
setCell(tst, (2,2), "X")
## blinker
setCell(tst, (5,5), "X")
setCell(tst, (6,5), "X")
setCell(tst, (4,5), "X")

### test 2 - tub & toad
tst2 = newBoard(10,10)
## tub
setCell(tst2, (0,1), "X")
setCell(tst2, (1,0), "X")
setCell(tst2, (1,2), "X")
setCell(tst2, (2,1), "X")
## toad
setCell(tst2, (6,5), "X")
setCell(tst2, (6,6), "X")
setCell(tst2, (6,7), "X")
setCell(tst2, (7,4), "X")
setCell(tst2, (7,5), "X")
setCell(tst2, (7,6), "X")

os.system("clear")
print("Block and Blinker")
printBoard(tst)
print()
print("Tub and Toad")
printBoard(tst2)
for i in range(30):
  time.sleep(.5)
  os.system("clear")
  tst = ageBoard(tst)
  tst2 = ageBoard(tst2)
  print("Block and Blinker")
  printBoard(tst)
  print()
  print("Tub and Toad")
  printBoard(tst2)


