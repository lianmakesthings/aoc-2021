
def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  # [[10 unique digits, four digits to decode], [,], [,]....]
  input = [x.split(" | ") for x in input]
  
  outputOnly = [x[1] for x in input]
  outputOnly = [x.split(" ") for x in outputOnly]
  
  return sum([sum(1 if len(y) in [2, 3, 4, 7] else 0 for y in x) for x in outputOnly])

def second(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  sum = 0
  for line in input:
    knownDigits = {} # digit: actualWrongSegments
    line = line.split(" | ")
    unknownDigits = [[c for c in x] for x in line[0].split()]
    output = [[c for c in x] for x in line[1].split()]

    knownDigits[1] = next(filter(lambda a: len(a) == 2, unknownDigits))
    unknownDigits.remove(knownDigits[1])

    knownDigits[4] = next(filter(lambda a: len(a) == 4, unknownDigits))
    unknownDigits.remove(knownDigits[4])

    knownDigits[7] = next(filter(lambda a: len(a) == 3, unknownDigits))
    unknownDigits.remove(knownDigits[7])

    knownDigits[8] = next(filter(lambda a: len(a) == 7, unknownDigits))
    unknownDigits.remove(knownDigits[8])

    knownDigits[9] = next(filter(lambda a: len(a) == 6 and all(s in a for s in knownDigits[4]), unknownDigits))
    unknownDigits.remove(knownDigits[9])

    knownDigits[0] = next(filter(lambda a: len(a) == 6 and all (s in a for s in knownDigits[1]), unknownDigits))
    unknownDigits.remove(knownDigits[0])

    knownDigits[6] = next(filter(lambda a: len(a) == 6, unknownDigits))
    unknownDigits.remove(knownDigits[6])

    knownDigits[3] = next(filter(lambda a: all(s in knownDigits[9] for s in a) and all(s in a for s in knownDigits[1]), unknownDigits))
    unknownDigits.remove(knownDigits[3])

    knownDigits[5] = next(filter(lambda a: all(s in knownDigits[9] for s in a), unknownDigits))
    unknownDigits.remove(knownDigits[5])

    knownDigits[2] = unknownDigits.pop()
  
    print(knownDigits.keys(), knownDigits.values())
    number = ""
    for o in output:
      for d in knownDigits.values():
        if all(s in d for s in o) and all(s in o for s in d):
          idx = list(knownDigits.values()).index(d)
          number += str(list(knownDigits.keys())[idx])
          break
    print(number)
    sum += int(number)
  return sum

print(second("input.txt"))
    
    