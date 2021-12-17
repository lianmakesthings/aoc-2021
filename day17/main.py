import re
def readFile(filepath):
  f = open(filepath, "r")
  content = f.readlines()
  return content[0]

def simulate(initialVelocity, target):
  currentPosition = (0, 0)
  currentVelocity = initialVelocity
  print("position before", currentPosition)
  
  inTarget = False
  pastTarget = False
  highestY = 0
  while not inTarget and not pastTarget:
    nextX = currentPosition[0]+currentVelocity[0]
    nextY = currentPosition[1]+currentVelocity[1]
    currentPosition = (nextX, nextY)
    highestY = max(highestY, nextY)

    dragX = 0 if currentVelocity[0] == 0 else 1
    velocityX = currentVelocity[0] + dragX if currentVelocity[0] < 0 else currentVelocity[0] - dragX
    velocityY = currentVelocity[1] - 1
    currentVelocity = (velocityX, velocityY)
    
    if currentPosition[0] in range(target[0][0], target[0][1]) and currentPosition[1] in range(target[1][0], target[1][1]):
      inTarget = True

    if currentPosition[1] < min(target[1]):
      pastTarget = True
    print("position after", currentPosition)
  return highestY if inTarget else False


def first(filepath):
  input = readFile(filepath)
  matches = re.findall("target area: x=(.+), y=(.+)", input)[0]
  target = [[int(x) for x in m.split('..')] for m in matches]
  print("target", target)
  initialVelocity = (6,9)

  highestY = simulate(initialVelocity, target)
  return highestY if highestY else 0