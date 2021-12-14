def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  polymer = input.pop(0)
  input.pop(0)
  insertionRules = {}
  for l in input:
    key, val = l.split(" -> ")
    insertionRules[key] = val

  steps = 10
  while steps > 0:
    newPolymer = ""
    for c in range(len(polymer)):
      pair = polymer[c:c+2]
      if len(pair) < 2:
        continue
      threesome = pair[0] + insertionRules[pair] + pair[1]
      if len(newPolymer) < 1:
        newPolymer = threesome
      else:
        newPolymer += threesome[1:3]
    polymer = newPolymer
    steps -= 1
  uniqueLetters = set(polymer)
  counts = [polymer.count(x) for x in list(uniqueLetters)]
  return max(counts) - min(counts)

print(first("input.txt"))
