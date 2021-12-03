import sys

def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath):
  lastVal = sys.maxsize
  increments = 0
  
  for line in readFile(filepath):
    val = int(line)
    if (val > lastVal):
      increments += 1

    lastVal = val

  return increments

def second(filepath):
  lines = readFile(filepath)

  lastSum = sys.maxsize
  increments = 0
  
  for i in range(0, len(lines)-2):
    currentSum = sum([int(x) for x in lines[i:i+3]])
    if (currentSum > lastSum):
      increments += 1

    lastSum = currentSum

  return increments
