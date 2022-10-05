import re


def find_name(line):
    pattern = r"[A-Za-z,\.]{2,50}||[A-Za-z]{2,50}"
    result = re.findall(pattern,line)
    
    return result


f = open("names.txt")
for line in f.readlines():
    result = find_name(line)
    for i in result:
      if (len(i)>0):
          print(i, end=" ")
          
    print()