import re

regex = re.compile('([a-z]+) (\\d)')

def readFile(filepath):
  f = open(filepath, "r")
  return f.readlines()

def parseCommand(line):
  matches = regex.findall(line)
  direction = matches[0][0]
  val = int(matches[0][1])

  return (direction, val)


def first(filepath):
  depth = 0
  position = 0

  for line in readFile(filepath):
    (direction, val) = parseCommand(line)

    if ('forward' == direction):
      position += val
    elif ('down' == direction):
      depth += val
    elif ('up' == direction):
      depth -= val
    else:
      print('something went wrong')

  return position * depth

def second(filepath):
  aim = 0
  position = 0
  depth = 0

  for line in readFile(filepath):
    (direction, val) = parseCommand(line)

    if ('forward' == direction):
      position += val
      depth += aim * val
    elif ('down' == direction):
      aim += val
    elif ('up' == direction):
      aim -= val
    else:
      print('something went wrong')

  return position * depth
