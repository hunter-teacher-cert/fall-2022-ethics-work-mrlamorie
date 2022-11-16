
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
      
