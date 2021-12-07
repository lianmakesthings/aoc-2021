import sys

def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath):
  input = [int(x) for x in readFile(filepath)[0].split(',')]
  minFuel = sys.maxsize
  for p in range(min(input), max(input)):
    fuel = sum([abs(p-x) for x in input])
    minFuel = min(minFuel, fuel)
  return minFuel

def second(filepath):
  input = [int(x) for x in readFile(filepath)[0].split(',')]
  minFuel = sys.maxsize
  for p in range(min(input), max(input)):
    fuel = sum([(abs(p-x)+1) * abs(p-x) / 2  for x in input])
    minFuel = min(minFuel, fuel)
  return minFuel

print(second("input.txt"))