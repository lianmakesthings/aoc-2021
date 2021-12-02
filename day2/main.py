import re

def first(filepath):
  f = open(filepath, "r")
  regex = re.compile('([a-z]+) (\\d)')
  depth = 0
  position = 0

  for line in f.readlines():
    matches = regex.findall(line)
    direction = matches[0][0]
    val = int(matches[0][1])

    if ('forward' == direction):
      position += val
    elif ('down' == direction):
      depth += val
    elif ('up' == direction):
      depth -= val
    else:
      print('something went wrong')

  return position * depth

print(first('input.txt'))
