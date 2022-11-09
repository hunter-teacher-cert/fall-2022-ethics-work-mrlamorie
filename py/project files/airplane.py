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

def get_number_economy_sold(economy_sold):
    """
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2

    Returns: the total number of seats sold
    """
    sold = 0
    for v in economy_sold.values():
        sold = sold + v
    return sold


def get_avail_seats(plane,economy_sold):
    """
    Parameters: plane : a list of lists representing plaine
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats that are "avail" or "win" 
           and removes the number of economy_sold seats
    """
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail

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


def purchase_economy_plus(plane,economy_sold,name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])

    
    # total unassigned seats
    seats = get_avail_seats(plane,economy_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane


    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat

    
    if random.randrange(100) > 30:
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]

        # randomzie it
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0])-1] == "win":
                plane[row][len(plane[0])-1] = name
                return  plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


# THIS WILL BE LEFT EMPTY FOR THE FIRST STAGE OF THE PROJECT
def seat_economy(plane,economy_sold,name):
    """
    This is mostly the same as the purchase_economy_plus routine but 
    just does the random assignment. 

    We use this when we're ready to assign the economy seats after most 
    of the economy plus seats are sold

 
    """
    rows = len(plane)
    cols = len(plane[0])

    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


def purchase_economy_block(plane,economy_sold,number,name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    seats_avail = get_total_seats(plane)
    seats_avail = seats_avail - get_number_economy_sold(economy_sold)

    if seats_avail >= number:
        economy_sold[name]=number
    return economy_sold


def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane

    comments interspersed in the code

    """

    
    economy_sold={}
    total_seats = get_total_seats(plane)
    


    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1
    u_number=1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    max_family_size = 3
    while total_seats > 1:
        r = random.randrange(100)
        if r > 30:
            plane = purchase_economy_plus(plane,economy_sold,"ep-%d"%ep_number)
            ep_number = ep_number + 1
            total_seats = get_avail_seats(plane,economy_sold)
        else:
            economy_sold = purchase_economy_block(plane,economy_sold,1+random.randrange(max_family_size),"u-%d"%u_number)
            u_number = u_number + 1

        
    # once the plane reaches a certian seating capacity, assign
    # seats to the economy plus passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section
    for name in economy_sold.keys():
        for i in range(economy_sold[name]):
            plane = seat_economy(plane,economy_sold,name)


    return plane
    




def group_size():
  # assuming ~ 50% solo, ~25% pairs, ~25% triplets
  size = random.randrange(4)
  if size == 0:
    size = 2 #test cost
    # size = 1
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
          
  # move on to groups of 2:           
  pairs = 0 # get number of pairs of seats
  for aisle in range(len(plane)):
    free_pairs = (free_in_aisle(plane, aisle)) // 2 # int division
    print('free pairs '+ str(free_pairs))
    pairs = pairs + free_pairs # update number of pairs of seats

  # now that we have the number of pairs, we can seat in pairs
  # as long as they still exist then seat split
  for i in range(len(groups_of_2)):
    name = groupSeat(groups_of_2[i], 'P')
    seated = False
    
    if pairs > 0: #fill the pairs first
      for aisle in range(len(plane)):
        if free_in_aisle(plane, aisle) > 2 and seated == False:
          fill_first_free(plane, aisle, name)
          fill_first_free(plane, aisle, name)
          pairs = pairs - 1
          seated = True

    elif seated == False: #fill remaining blocks
      print('elif fired off')
      to_be_seated = 2
      for aisle in range(len(plane)):
        free = free_in_aisle(plane, aisle)
        while to_be_seated > 0 and free > 0:
          
          fill_first_free(plane, aisle, name)
          free = free - 1
          to_be_seated = to_be_seated -1    
          seated = True
    else:
      continue
  
  for i in range(len(solos)):
    name = groupSeat(solos[i], 'S')
    seated = False
    for aisle in range(len(plane)):
      if free_in_aisle(plane, aisle) and seated == False:
        fill_first_free(plane, aisle, name)
        seated = True
   
          
  return plane
  

def main():
    length = 10
    width = 5
    plane = create_plane(length,width)
    print(get_plane_string(fill_plane2(plane)))

if __name__=="__main__":
    main()