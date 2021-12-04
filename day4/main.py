def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

boardSize = 5

def checkForWin(marked, lastBoardIndex):
  won = False
  for b in range(0, lastBoardIndex):
    markedInBoard = [x for x in marked if x[0] == b]
    if len(markedInBoard) < boardSize:
      continue
    for r in range(0, boardSize):
      row = [x for x in markedInBoard if x[1] == r]
      if len(row) >= boardSize:
        won = b
        continue
    if False != won:
      continue

    for c in range(0, boardSize):
      column = [x for x in markedInBoard if x[2] == c]
      if len(column) >= boardSize:
        won = b
        continue
    if False != won:
      continue
  return won

def first(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath) if "\n" != x]
  drawnNumbers = input.pop(0).split(",")
  boards = []
  lastBoardIndex = int(len(input)/boardSize)
  for r in range(0, len(input)):
    row = [x for x in input[r].split(" ") if len(x) > 0]
    for c in range(0, boardSize):
      boards.append((int(r/boardSize), r%boardSize, c, int(row[c])))

  marked = []
  won = False
  number = 0
  while(False == won):
    number = int(drawnNumbers.pop(0))
    marked += [x for x in boards if x[3] == number]
    boards = [x for x in boards if x[3] != number]
    won = checkForWin(marked, lastBoardIndex)

  winningBoard = [x for x in boards if won == x[0]]
  unmarkedNumbers = [x for x in winningBoard if x not in marked]
  sumUnmarked = sum([x[3] for x in unmarkedNumbers])

  return sumUnmarked * number

def second(filepath):
  input = [x.replace("\n", "") for x in readFile(filepath) if "\n" != x]
  drawnNumbers = input.pop(0).split(",")
  boards = []
  lastBoardIndex = int(len(input)/boardSize)
  for r in range(0, len(input)):
    row = [x for x in input[r].split(" ") if len(x) > 0]
    for c in range(0, boardSize):
      boards.append((int(r/boardSize), r%boardSize, c, int(row[c])))

  marked = []
  number = int(drawnNumbers.pop(0))
  winningBoard = []
  while len(boards) > 0:
    won = False
    while(type(won) == bool):
      marked += [x for x in boards if x[3] == number]
      boards = [x for x in boards if x[3] != number]
      won = checkForWin(marked, lastBoardIndex)
      if False == won:
        number = int(drawnNumbers.pop(0))
    winningBoard = [x for x in boards if won == x[0]]
    unmarkedNumbers = [x for x in winningBoard if x not in marked]
    sumUnmarked = sum([x[3] for x in unmarkedNumbers])
    boards = [x for x in boards if x not in winningBoard]
    marked = [x for x in marked if x[0] is not won]

  return sumUnmarked * number

print(second("input.txt"))