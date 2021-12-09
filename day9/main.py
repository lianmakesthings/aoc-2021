import math

def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def sortByVal(p):
  return p[2]

def buildMap(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  heightMap = []
  for x in range(len(input)):
    line = input[x]
    for y in range(len(line)):
      heightMap.append((x, y, int(line[y])))
  heightMap.sort(key=sortByVal, reverse=True)
  return heightMap

def getAdjacentPoints(p, map):
  pointX = p[0]
  pointY = p[1]
  return [x for x in map if (p is not x and ((x[0] == pointX and x[1] in range(pointY-1, pointY+2)) or (x[1] == pointY and x[0] in range(pointX-1, pointX+2))))]

def calcLowPoints(heightMap):
  lowPoints = []
  unchecked = heightMap
  while len(unchecked) > 0:
    point = unchecked.pop()
    adjacentPoints = getAdjacentPoints(point, heightMap)
    if all(point[2] < p[2] for p in adjacentPoints):
      lowPoints.append(point)
      unchecked = [x for x in unchecked if not x in adjacentPoints]
  return lowPoints

def first(filepath):
  heightMap = buildMap(filepath)
  lowPoints = calcLowPoints(heightMap)
  return sum([x[2] for x in lowPoints]) + len(lowPoints)

def second(filepath):
  heightMap = buildMap(filepath)
  lowPoints = calcLowPoints(heightMap)
  basinSize = []
  for p in lowPoints:
    basin = {p}
    adjacentPointsNotNine = [x for x in getAdjacentPoints(p, heightMap) if x[2] < 9 and x not in basin]
    
    while len(adjacentPointsNotNine) > 0:
      basin.update(adjacentPointsNotNine)
      adjacentPointsNotNine = [i for s in [getAdjacentPoints(x, heightMap) for x in adjacentPointsNotNine] for i in s if i[2] < 9 and i not in basin]
      
    basinSize.append(len(basin))
  basinSize.sort(reverse=True)
  
  return math.prod(basinSize[:3])

print(second("input.txt"))