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

def setCell(board, row, col, sym):
  """A function that takes in 2d array "board" and sets the string value of a
  cell at board[row][col] to symbol sym. """

  board[row][col] = sym

### test code
tst = newBoard(10,5)
setCell(tst, 1, 2, "X")
printBoard(tst)
