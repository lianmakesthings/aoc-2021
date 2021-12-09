def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def sortByVal(p):
  return p[2]

def first(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  heightMap = []
  for x in range(len(input)):
    line = input[x]
    for y in range(len(line)):
      heightMap.append((x, y, int(line[y])))
  
  
  lowPoints = [] 
  heightMap.sort(key=sortByVal, reverse=True)
  unchecked = heightMap
  while len(unchecked) > 0:
    point = unchecked.pop()
    pointX = point[0]
    pointY = point[1]
    pointValue = point[2]
    adjacentPoints = [x for x in heightMap if (point is not x and ((x[0] == pointX and x[1] in range(pointY-1, pointY+2)) or (x[1] == pointY and x[0] in range(pointX-1, pointX+2))))]
    if all(pointValue < p[2] for p in adjacentPoints):
      lowPoints.append(point)
      unchecked = [x for x in unchecked if not x in adjacentPoints]
  return sum([x[2] for x in lowPoints]) + len(lowPoints)

print(first("input.txt"))