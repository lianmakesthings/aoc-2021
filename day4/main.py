def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

boardSize = 5

def first(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath) if "\n" != x]
  drawnNumbers = input.pop(0).split(",")
  
  boards = []
  lastBoardIndex = int(len(input)/boardSize)
  for r in range(0, len(input)):
    row = list(filter(lambda a: len(a) > 0, input[r].split(" ")))
    for c in range(0, boardSize):
      boards.append((int(r/boardSize), r%boardSize, c, int(row[c])))

  marked = []
  
  won = False
  number = 0
  while(False == won):
    number = int(drawnNumbers.pop(0))
    for n in list(filter(lambda a: a[3] == number, boards)):
      marked.append(n)
    
    for b in range(0, lastBoardIndex):
      markedInBoard = list(filter(lambda a: a[0] == b, marked))
      if len(markedInBoard) < boardSize:
        continue
      for r in range(0, boardSize):
        row = list(filter(lambda a: a[1] == r, markedInBoard))
        if len(row) >= boardSize:
          won = b
          continue

      if False != won:
        continue
      for c in range(0, boardSize):
        column = list(filter(lambda a: a[2] == c, markedInBoard))
        if len(column) >= boardSize:
          won = b

  winningBoard = [x for x in boards if won == x[0]]
  unmarkedNumbers = list(filter(lambda a: a not in marked, winningBoard))
  sumUnmarked = sum([x[3] for x in unmarkedNumbers])

  return sumUnmarked * number

print(first("input.txt"))
