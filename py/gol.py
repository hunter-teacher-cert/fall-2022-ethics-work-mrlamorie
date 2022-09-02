# gol.py
# William LaMorie
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

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
      
### test code
tst = newBoard(10,5)
setCell(tst, (5,2), "X")
setCell(tst, (6,2), "X")
setCell(tst, (4,2), "X")
printBoard(tst)
print(countNeighbors(tst, (5,2), "X"))
print(countNeighbors(tst, (6,2), "X"))
