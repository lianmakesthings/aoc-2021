def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def loop(fishMap, days):
  while days > 0:
    newFishMap = {}
    for x in range(0, 9):
      newFishMap[8] = fishMap[0]
      if x > 0:
        newFishMap[x-1] = fishMap[x] + newFishMap[x-1] if x-1 in newFishMap else fishMap[x]
      else:
        newFishMap[6] = fishMap[x]

    fishMap = newFishMap
    days -= 1

  return newFishMap

def first(filepath):
  fishList = [int(f) for f in readFile(filepath)[0].split(",")]
  fishMap = {}
  for x in range(0, 9):
    fishMap[x] = sum(1 if f == x else 0 for f in fishList)
  newFishMap = loop(fishMap, 80)

  return sum(newFishMap.values())

def second(filepath):
  fishList = [int(f) for f in readFile(filepath)[0].split(",")]
  fishMap = {}
  for x in range(0, 9):
    fishMap[x] = sum(1 if f == x else 0 for f in fishList)
  newFishMap = loop(fishMap, 256)
  return sum(newFishMap.values())

print(second("input.txt"))