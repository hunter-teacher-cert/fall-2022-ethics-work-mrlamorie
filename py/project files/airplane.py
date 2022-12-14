"""
This version of the plane filling program looks to keep groups togather based on a first come, first serve model
Economy plus has been removed, with the underling idea
that we would have regular economy and a discount for later fill in.

Assumptions - to stay in line with the instructor provided
version - we will assume the plane can fit less then 100
people, and no more than 3 are in a group

General Algorithm -
1. Build plane
2. Get total number of seats
3. Until seats full -
   A. Get next customer or customer group, add to seating order
   B. If too large to seat, pass
4. Seat customers - 
   A. sub 1 - as no priority is given to location, only trying
   to seat groups, groups of 3 in order then groups of
   2, seat groups from left to right, starting with 
   groups in order of "booked" with the
   groups first then fill with individals.
   A. sub 2 - Check for side by side seats for groups of 2 before
   moving on to unpaired in case of wierd scenes where we have a 
   number of groups of 2 that need to be split
   B. Most groups should be able to be sat in groups. 
   If not, then randomly seat them (no further chunking
   of note should be available now)
   C. Fill in remaining seats with individuals
5. Return filled plane list. (Also return number of failed bookings?)
      

"""
import random


def create_plane(rows,cols):
    """

    returns a new plane of size rowsxcols

    A plane is represented by a list of lists. 

    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane


def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s


def group_size():
  # assuming ~ 50% solo, ~25% pairs, ~25% triplets
  size = random.randrange(4)
  if size == 0:
    size = 1
  return size

def number_aisles(plane):
  asiles = 0
  for i in plane:
    asiles = asiles + 1
  return asiles

def free_in_aisle(plane, aisle):
  free = 0
  for i in plane[aisle]:
    if i == "win" or i == "avail":
      free = free + 1
  return free


def fill_first_free(plane, aisle, fill):
  for seat in range(len(plane[aisle])):
    filled = False
    if plane[aisle][seat] == 'avail' or plane[aisle][seat] == 'win':
      plane[aisle][seat] = fill
      break
      
def groupSeat(groupNum, type='S'):
  '''
  Assumes we need less than 100 total seating "groups"
  '''
  if groupNum < 10:
    return type + "0" + str(groupNum) 
  else:
    return type + str(groupNum)

def fill_plane2(plane):
  unsold = get_total_seats(plane) #keep booking until full
  missed_customers = 0 # to see how many we miss
  groups = [] # list of bookings in order

  asiles = number_aisles(plane) # for some short cuts
  
  while unsold > 0:
    nextgroup = group_size()
    if nextgroup <= unsold:
      unsold = unsold - nextgroup
      groups.append(nextgroup)
    else:
      missed_customers = missed_customers + nextgroup

  groups_of_3 = [] # indexes of groups of 3 in order
  groups_of_2 = [] # indexes of groups of 2 in order
  solos = [] #indexes of solos in order.
  
  #find our groupings
  for i in range(len(groups)): 
    if groups[i] == 1:
      solos.append(i)
    elif groups[i] == 2:
      groups_of_2.append(i)
    else:
      groups_of_3.append(i)

  print('Number of passengers: ' + str(sum(groups)))
  print('indexes of solos:')
  print(solos)
  print('indexes of pairs:')
  print(groups_of_2)
  print('indexes of trios:')
  print(groups_of_3)
  # seat groups of 3
  for i in range(len(groups_of_3)):
    #generate name for group to show off how fancy we are
    name = groupSeat(groups_of_3[i], 'T')
    
    # do easy ones first - full in a row
    if i < asiles:

      #seating first, so we can always use indexes 0,1,2
      plane[i][0] = name
      plane[i][1] = name
      plane[i][2] = name

    # fill in the remaineder of these
    else:
      to_be_seated = 3
      for aisle in range(len(plane)):
        free = free_in_aisle(plane, aisle)
        while to_be_seated > 0 and free > 0:
          fill_first_free(plane, aisle, name)
          free = free - 1
          to_be_seated = to_be_seated -1

  #seat pairs
  for i in range(len(groups_of_2)):
    name = groupSeat(groups_of_2[i], 'P')
    seated = False
    #seat in pair if doable
    for aisle in range(len(plane)):
      if free_in_aisle(plane, aisle) >= 2 and seated == False:
        fill_first_free(plane, aisle, name)
        fill_first_free(plane, aisle, name)
        seated = True

    # unseated duo handling
    if seated == False:
      print('split pair')
      to_be_seated = 2
      for aisle in range(len(plane)):
        if free_in_aisle(plane, aisle) > 0 and to_be_seated > 0:
          fill_first_free(plane, aisle, name)
          to_be_seated = to_be_seated -1
   
  #seat solo passengers
  for i in range(len(solos)):
    name = groupSeat(solos[i], 'S')
    seated = False
    for aisle in range(len(plane)):
      if free_in_aisle(plane, aisle) and seated == False:
        fill_first_free(plane, aisle, name)
        seated = True #halt, we found a seat
          
  return plane
  

def main():
    length = 10
    width = 5
    plane = create_plane(length,width)
    print(get_plane_string(fill_plane2(plane)))

if __name__=="__main__":
    main()
