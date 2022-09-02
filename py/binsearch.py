# binsearch.py
# William LaMorie
# CSCI 77800 Fall 2022
# collaborators: NA
# consulted: NA

def binarySearch(struct, val):
  """ A binary search that should works on a list or a tuple, or a number keyed 
  and order dictionary of ints, returns index of value or -1 if not found """
  low = 0
  high = len(struct)
  mid = (low + high) //2

  while True:
    if high <= low:  # base case, does not exist on list
      return -1
    elif struct[mid] == val: #found
      return mid
    elif struct[mid] > val: #too high
      high = mid -1
    else: #too low
      low = mid +1
    
    mid = (low + high) //2 #update mid


## list test:
print("List test")
tst = [0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binarySearch(tst, 5)) #should be 6
print(binarySearch(tst, 0)) #should be 0 or 1
print(binarySearch(tst, 55)) #should be -1
print(binarySearch(tst, -22)) #should be -1

## tuple test:
print("Tuple test")
tst2 =(0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(binarySearch(tst2, 5)) #should be 6
print(binarySearch(tst2, 0)) #should be 0 or 1
print(binarySearch(tst2, 55)) #should be -1
print(binarySearch(tst2, -22)) #should be -1

## dict test?
print("OMG dictionaries are ordered now test")
tst3 = {0:0, 1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9, 11:10, 12:11, 13:12, 14:13, 15:14, 16:15, 17:16, 18:17, 19:18, 20:19, 21:20}
print(binarySearch(tst3, 5)) #should be 6
print(binarySearch(tst3, 0)) #should be 0 or 1
print(binarySearch(tst3, 55)) #should be -1
print(binarySearch(tst3, -22)) #should be -1