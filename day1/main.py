import sys

def first(filepath):
  f = open(filepath, "r")
  lastVal = sys.maxsize
  increments = 0
  
  for line in f.readlines():
    val = int(line)
    if (val > lastVal):
      increments += 1

    lastVal = val

  return increments

def second(filepath):
  f = open(filepath, "r")
  lines = f.readlines()

  lastSum = sys.maxsize
  increments = 0

  for i in range(0, len(lines)-2):
    val = int(lines[i])
    val1 = int(lines[i+1])
    val2 = int(lines[i+2])
    sum = val + val1 + val2
    if (sum > lastSum):
      increments += 1

    lastSum = sum

  return increments

print(second("input.txt"))
