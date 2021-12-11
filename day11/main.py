def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def getAdjacentPoints(p, map):
  pointX = p[0]
  pointY = p[1]
  return [x for x in map if (p is not x and ((x[0] == pointX and abs(x[1]-pointY) == 1) or (x[1] == pointY and abs(x[0]-pointX) == 1) or (abs(x[0]-pointX) == 1 and abs(x[1]-pointY) == 1)))]

def first(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  map = []
  for x in range(len(input)):
    line = input[x]
    for y in range(len(line)):
      map.append((x, y, int(line[y])))

  steps = 100
  flashCount = 0
  while steps > 0:
    map = [(x[0], x[1], x[2]+1) for x in map]
    print("first increase", map)
    flashing = [(x[0], x[1]) for x in map if x[2] > 9]
    print("flashing", flashing)

    for o in flashing:
      adjacent = getAdjacentPoints(o, map)
      #print(o, adjacent)
      map = [(x[0], x[1], x[2]+1) if x in adjacent else x for x in map]
      #print("increase adjacent", map)

      newFlashes = [(x[0], x[1]) for x in adjacent if x[2] > 8 and (x[0], x[1]) not in flashing]
      #print("newFlashes", newFlashes)
      flashing += [x for x in newFlashes]
      #print("flashing + newFlashes", flashing)
      
    map = [(x[0], x[1], 0) if x[2]>9 else x for x in map]
    
    flashCount += len(flashing)
    steps -= 1
  return flashCount

def second(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  map = []
  for x in range(len(input)):
    line = input[x]
    for y in range(len(line)):
      map.append((x, y, int(line[y])))
  
  synced = False
  steps = 0
  while synced == False:
    steps += 1
    map = [(x[0], x[1], x[2]+1) for x in map]
    flashing = [(x[0], x[1]) for x in map if x[2] > 9]

    for o in flashing:
      adjacent = getAdjacentPoints(o, map)
      map = [(x[0], x[1], x[2]+1) if x in adjacent else x for x in map]

      newFlashes = [(x[0], x[1]) for x in adjacent if x[2] > 8 and (x[0], x[1]) not in flashing]
      #print("newFlashes", newFlashes)
      flashing += [x for x in newFlashes]
      #print("flashing + newFlashes", flashing)
      
    map = [(x[0], x[1], 0) if x[2]>9 else x for x in map]
    
    if len(flashing) == len(map):
      synced = True
  return steps
print(second("input.txt"))