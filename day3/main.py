def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def mostCommonBit(list):
  bit = max(set(list), key=list.count)
  if min(set(list), key=list.count) == bit:
      bit = "1"
  return bit

def leastCommonBit(list):
  bit = min(set(list), key=list.count)
  if max(set(list), key=list.count) == bit:
      bit = "0"
  return bit


def first(filepath):
  lines = [line.replace("\n", "") for line in readFile(filepath)]
  gamma = ""
  epsilon = ""
  
  for i in range(len(lines[0])):
    bitColumn = [x[i] for x in lines]
    gamma += mostCommonBit(bitColumn)
    epsilon += leastCommonBit(bitColumn)
  
  return int(gamma, 2) * int(epsilon, 2)

def second(filepath):
  allLines = [line.replace("\n", "") for line in readFile(filepath)]
  
  lines = allLines
  for i in range(len(lines[0])):
    if 1 == len(lines):
      break

    bitColumn = [x[i] for x in lines]
    lines = [x for x in lines if x[i] == mostCommonBit(bitColumn)]
  oxy = int(lines[0], 2)

  lines = allLines
  for i in range(len(lines[0])):
    if 1 == len(lines):
      break

    bitColumn = [x[i] for x in lines]
    lines = [x for x in lines if x[i] == leastCommonBit(bitColumn)]
  co2 = int(lines[0], 2)

  return oxy * co2

print(second("input.txt"))