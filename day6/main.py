def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def first(filepath):
  days = 80
  fish = [int(f) for f in readFile(filepath)[0].split(",")]

  while days > 0:
    newFishCount = sum(1 if f == 0 else 0 for f in fish)
    fish = [f-1 if f > 0 else 6 for f in fish]
    fish += [8 for f in range(newFishCount)]
    days = days-1

  return len(fish)

print(first("input.txt"))