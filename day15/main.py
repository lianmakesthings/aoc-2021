import sys
def readFile(filepath):
  f = open(filepath, "r")
  content = f.readlines()
  return [x.replace("\n", "") for x in content]

def getRisk(map, coord):
  point = [x for x in map if x[0] == coord[0] and x[1] == coord[1]]
  return point[0][2]

def getAdjacentPoints(map, coord):
  return [x for x in map if (x[0] == coord[0] and abs(coord[1]-x[1]) == 1) or (x[1] == coord[1] and abs(coord[0]-x[0]) == 1)]

def hasPoint(map, coord):
  points = [x for x in map if x[0] == coord[0] and x[1] == coord[1]]
  return map.index(points[0]) if len(points) > 0 else False

def buildRiskMap(map):
  maxX = max([x[0] for x in map])
  maxY = max([x[1] for x in map])
  riskmap = [(maxX, maxY, 0)]
  for currentPoint in map:
    print(map.index(currentPoint), len(map))
    adjacentPoints = getAdjacentPoints(map, currentPoint)
    newRiskPoints = [(x[0], x[1], getRisk(riskmap, currentPoint)+currentPoint[2]) for x in adjacentPoints]
    lowestRisk = min([x[2] for x in adjacentPoints])
    for p in newRiskPoints:
      index = hasPoint(riskmap, p)
      if index and getRisk(riskmap, p) > p[2]:
        riskmap.pop(index)
        riskmap.append(p)
      elif not hasPoint(riskmap, p):
        riskmap.append(p)

  return riskmap


def first(filepath):
  input = readFile(filepath)
  map = []
  for y in range(len(input)):
    line = input[y]
    for x in range(len(input[0])):
      map.append((x, y, int(line[x])))
  map.reverse()
  riskmap = buildRiskMap(map)
  print(riskmap)
  return [x[2] for x in riskmap if x[0] == 0 and x[1] == 0][0]

def second(filepath):
  input = readFile(filepath)
  map = []
  tileY = len(input)
  tileX = len(input[0])
  totalY = tileY * 5
  totalX = tileX * 5
  yOffset = 0
  for y in range(totalY):
    line = input[y%tileY]
    yOffset = y // tileY
    for x in range(totalX):
      xOffset = x // tileX
      value = int(line[x%tileX]) + xOffset + yOffset
      value = value - 9 if value > 9 else value
      map.append((x, y, value))
    xOffset += 1
  yOffset += 1
  map.reverse()

  riskmap = buildRiskMap(map)
  return [x[2] for x in riskmap if x[0] == 0 and x[1] == 0][0]

#print(first("input.txt"))

  