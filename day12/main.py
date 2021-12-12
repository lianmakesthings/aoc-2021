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
    if start != "end":
      newPaths = [p + [x] for x in pathMap[start] if not (x.islower() and x in p)]
      paths += [x for x in newPaths if x not in paths]
  
  return len([x for x in paths if x[-1] == "end"])

def second(filepath):
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
  print(pathMap)
  paths = [["start"]]
  for p in paths:
    start = p[-1]
    if start != "end":
      newPaths = [p + [x] for x in pathMap[start] if not (x == "start" or (x.islower() and p.count(x) > 0 and max([p.count(a) for a in p if a.islower()]) > 1))]
      paths += [x for x in newPaths if x not in paths]

  return len([x for x in paths if x[-1] == "end"])

print(second("input.txt"))