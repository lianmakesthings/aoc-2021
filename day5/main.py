import re

def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath):
  regex = "([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)"
  input = [x for x in readFile(filepath)]
  covered = {}
  for l in input:
    coords = re.findall(regex, l)
    start = (int(coords[0][0]), int(coords[0][1]))
    end = (int(coords[0][2]), int(coords[0][3]))
    if start[0] == end[0]:
      for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
        coord = (start[0], y)
        if coord not in covered:
          covered[coord] = 1
        else:
          covered[coord] += 1
    elif start[1] == end[1]:
      for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
        coord = (x, start[1])
        if coord not in covered:
          covered[coord] = 1
        else:
          covered[coord] += 1

  return len([x for x in list(covered.values()) if x > 1])

print(first("input.txt"))