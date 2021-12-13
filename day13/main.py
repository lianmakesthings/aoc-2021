import re
def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  dots = [(int(y[0]), int(y[1])) for y in [x.split(",") for x in input if "," in x]]
  folds = [re.findall("([x|y])=([0-9]*)", x)[0] for x in input if "=" in x]
  

  for f in folds:
    index = 0 if f[0] == "x" else 1
    line = int(f[1])

    newDots = [d for d in dots if d[index] < line]
    dotsToFold = [d for d in dots if d not in newDots]
    newDots += [(d[0], (d[1] - 2*(d[1] - line))) if index == 1 else (d[0] - 2*(d[0] - line), d[1]) for d in dotsToFold]
    dots = list(set(newDots))
    break
  return len(dots)

def second(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  dots = [(int(y[0]), int(y[1])) for y in [x.split(",") for x in input if "," in x]]
  folds = [re.findall("([x|y])=([0-9]*)", x)[0] for x in input if "=" in x]
  
  for f in folds:
    index = 0 if f[0] == "x" else 1
    line = int(f[1])
    newDots = [d for d in dots if d[index] < line]
    dotsToFold = [d for d in dots if d not in newDots]
    newDots += [(d[0], (d[1] - 2*(d[1] - line))) if index == 1 else (d[0] - 2*(d[0] - line), d[1]) for d in dotsToFold]
    dots = list(set(newDots))

  highestX = max([x[0] for x in dots])
  highestY = max([x[1] for x in dots])
  print(highestX, highestY)
  print(dots)
  
  for y in range(highestY+1):
    lineToRender = ""
    for x in range(highestX+1):
      lineToRender += "#" if (x, y) in dots else "."
    print(lineToRender)

second("input.txt")
  