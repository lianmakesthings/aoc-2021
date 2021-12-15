import sys
def readFile(filepath):
  f = open(filepath, "r")
  content = f.readlines()
  return [x.replace("\n", "") for x in content]

def getRisk(map, coord):
  point = [x for x in map if x[0] == coord[0] and x[1] == coord[1]]
  return point[0][2]

def getAdjacentPoints(map, coord):
  return [x for x in map if (x[0] == coord[0] and abs(x[1]-coord[1]) == 1) or (x[1] == coord[1] and abs(x[0]-coord[0]) == 1)]

def hasPoint(map, coord):
  points = [x for x in map if x[0] == coord[0] and x[1] == coord[1]]
  return map.index(points[0]) if len(points) > 0 else False

def buildRiskMap(map):
  maxX = max([x[0] for x in map])
  maxY = max([x[1] for x in map])
  riskmap = [(maxX, maxY, 0)]
  for nextPoint in map:
    print(map.index(nextPoint), len(map))
    newRiskPoints = [(x[0], x[1], getRisk(riskmap, nextPoint)+nextPoint[2]) for x in getAdjacentPoints(map, nextPoint)]
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
  return [x[2] for x in riskmap if x[0] == 0 and x[1] == 0][0]

#print(first("input.txt"))

  