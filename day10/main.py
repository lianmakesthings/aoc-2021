def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

charPairs = {
  "(" : ")",
  "[" : "]",
  "{" : "}",
  "<" : ">"
}
pointsForCharPartOne = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

def first(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  expectedClosingChars = []
  score = 0
  for line in input:
    for char in line:
      if char in charPairs.keys():
        expectedClosingChars.insert(0, charPairs[char])
      elif char in charPairs.values() and char == expectedClosingChars.pop(0):
        continue
      else:
        score += pointsForCharPartOne[char]
  return score

pointsForCharPartTwo = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4
}

def second(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath)]
  scores = []
  for line in input:
    expectedClosingChars = []
    score = 0
    corrupted = False
    for char in line:
      if char in charPairs.keys():
        expectedClosingChars.insert(0, charPairs[char])
      elif char in charPairs.values() and char == expectedClosingChars[0]:
        expectedClosingChars.pop(0)
      elif char in charPairs.values() and char != expectedClosingChars[0]:
        corrupted = True
      if corrupted:
        continue
    if not corrupted:
      for c in expectedClosingChars:
        score = score * 5
        score += pointsForCharPartTwo[c]
      scores.append(score)
  
  scores.sort()
  return scores[len(scores)//2]

print(second("input.txt"))
        

