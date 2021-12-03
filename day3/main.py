def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()


def first(filepath):
  lines = [line.replace("\n", "") for line in readFile(filepath)]
  gamma = ""
  epsilon = ""
  
  for i in range(len(lines[0])):
    bitColumn = [x[i] for x in lines]
    gamma += max(set(bitColumn), key=bitColumn.count)
    epsilon += min(set(bitColumn), key=bitColumn.count)
  
  return int(gamma, 2) * int(epsilon, 2)

def second(filepath):
  allLines = [line.replace("\n", "") for line in readFile(filepath)]
  
  lines = allLines
  for i in range(len(lines[0])):
    if 1 == len(lines):
      break

    bitColumn = [x[i] for x in lines]
    commonBit = max(set(bitColumn), key=bitColumn.count)
    if min(set(bitColumn), key=bitColumn.count) == commonBit:
      leastCommonBit = "1"

    lines = [x for x in lines if x[i] == commonBit]
  oxy = int(lines[0], 2)
  
  lines = allLines
  for i in range(len(lines[0])):
    if 1 == len(lines):
      break

    bitColumn = [x[i] for x in lines]
    leastCommonBit = min(set(bitColumn), key=bitColumn.count)
    if max(set(bitColumn), key=bitColumn.count) == leastCommonBit:
      leastCommonBit = "0"
  
    lines = [x for x in lines if x[i] == leastCommonBit]
  co2 = int(lines[0], 2)

  return oxy * co2

print(second("input.txt"))