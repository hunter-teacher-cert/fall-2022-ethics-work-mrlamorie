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
  return [[sym]*cols] * rows  
  
def printBoard(board):
  """A function to print a 2d array as a grid"""
  for row in board:
    for col in row:
      print(col, end=' ')
    print()

tst = newBoard(10,5)
printBoard(tst)