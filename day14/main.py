
def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath, steps):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  
  stringBeginning = input.pop(0)
  firstChar = stringBeginning[0]
  lastChar = stringBeginning[-1]
  polymer = {}
  for i in range(len(stringBeginning)):
    if i < len(stringBeginning)-1:
      pair = stringBeginning[i:i+2]
      count = polymer[pair] +1 if pair in polymer else 1
      polymer[pair] = count
  input.pop(0)

  insertionRules = {}
  for l in input:
    key, val = l.split(" -> ")
    insertionRules[key] = [key[0]+val, val+key[1]]
  while steps > 0:
    pairs = [x for x in polymer.keys() if polymer[x] > 0]
    newPolymer = {}
    
    for p in pairs:
      for np in insertionRules[p]:
        count = newPolymer[np]+polymer[p] if np in newPolymer else polymer[p]
        newPolymer[np] = count
      
    polymer = newPolymer
    steps -= 1

  letterCount = {}
  for pair in polymer.keys():
    for c in pair:
      count = letterCount[c]+polymer[pair] if c in letterCount else polymer[pair]
      letterCount[c] = count

  letterCount[firstChar] = letterCount[firstChar]+1
  letterCount[lastChar] = letterCount[lastChar]+1

  letterCount = [x/2 for x in letterCount.values()]
  return max(letterCount) - min(letterCount)

print(first("input.txt", 40))
