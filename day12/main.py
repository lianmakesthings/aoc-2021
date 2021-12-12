def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  pathMap = {}
  for line in input:
    start, end = line.split("-")
    if start in pathMap:
      pathMap[start].append(end)
    else:
      pathMap[start] = [end]
    
    if not (start == "start" or end == "end"):
      if end in pathMap:
        pathMap[end].append(start)
      else:
        pathMap[end] = [start]

  smallCaves = [x for x in pathMap.keys() if x.islower() and not (x == "start" or x == "end")]
  for c in smallCaves:
    if len(pathMap[c]) == 1 and pathMap[c][0].islower():
      pathMap[pathMap[c][0]] = [x for x in pathMap[pathMap[c][0]] if x != c]
      pathMap.pop(c)
  
  paths = [["start"]]
  for p in paths:
    start = p[-1]
    pathsEndInStart = [x for x in paths if x[-1] == start]
    if start != "end":
      newPaths = [y + [x] for x in pathMap[start] for y in pathsEndInStart if not (x.islower() and x in y)]
      paths += [x for x in newPaths if x not in paths]
  
  return sum(1 if x[0] == "start" and x[-1] == "end" else 0 for x in paths)

print(first("input.txt"))

