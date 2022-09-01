# nim.py
# William LaMorie
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

import random

"""
bag contains 12 stones initially
a move consists of removing 1-3 stones from the bag
prompt user for number of stones they wish to remove each turn
tell user how many stones the AI removed and how many stones remain
facilitate play until human or AI wins, and announce winner
"""

stones = 12 # number of total stones @ start

while stones > 0:
  # start of turn
  print("There are currently " + str(stones) + " stones left.")

  ### player move
  maxStones = 3 
  #check to see if there are less than 3 stones left for string format
  if stones < maxStones:
    maxStones = stones

  #ask player to take stones.
  #ASSUMES PLAYER ENTERS A VALID NUMBER
  stonesTaken = input("How many (1-"+ str(maxStones) + ") stones would you like to take? ")
  stonesTaken = int(stonesTaken)


  #number range checking
  while stonesTaken > maxStones:
    stonesTaken = input("Please pick from 1 - " + str(maxStones) + " stones: ")
    stonesTaken = int(stonesTaken)

  
  stones = stones - stonesTaken
  
  if stones <= 0:
    print("Player Wins!")
    break

  ### end player move

  ### AI move -
  if stones <= 3:  # win if 3 or less
    stonesTaken = stones
  else: # otherwise random pull
    stonesTaken = random.randrange(1,4)

  # display computer move
  print("The computer takes " + str(stonesTaken) + " stones.")
  stones = stones - stonesTaken

  if stones == 0:
    print("Computer Wins!")
    break
  ### end AI move
    

