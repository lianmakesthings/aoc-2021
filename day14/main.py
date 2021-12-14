def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath, steps):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  polymer = input.pop(0)
  input.pop(0)
  insertionRules = {}
  for l in input:
    key, val = l.split(" -> ")
    insertionRules[key] = val

  while steps > 0:
    print(steps)
    toReplace = {}
    for key in insertionRules.keys():
      occurences = [i for i in range(len(polymer)) if polymer.startswith(key, i)]
      for i in occurences:
        toReplace[i+1] = insertionRules[key]
    
    toReplaceIndices = list(toReplace.keys())
    toReplaceIndices.sort()
    print(len(toReplaceIndices))
    for i in toReplaceIndices:
      polymer = polymer[:i+toReplaceIndices.index(i)] + toReplace[i] + polymer[i+toReplaceIndices.index(i):]

    steps -= 1
  uniqueLetters = set(polymer)
  counts = [polymer.count(x) for x in uniqueLetters]
  return max(counts) - min(counts)

print(first("input.txt", 40))