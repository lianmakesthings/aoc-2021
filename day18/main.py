import re
def readFile(filepath):
  f = open(filepath, "r")
  content = f.readlines()
  return [x.replace("\n", "") for x in content]

def first(filepath):
  input = readFile(filepath)
  number = input[0]
  print(number)
  print(explode(number))

def explode(number):
  matches = re.findall("([0-9]*)(]*),*(\\[{4,})([0-9])+,([0-9]+)],([0-9]+)", number)
  old = ""
  new = ""
  if len(matches) > 0:
    matches = matches[0]
    print(matches)
    left = int(matches[3])
    left += int(matches[0]) if len(matches[0]) > 0 else 0
    right = int(matches[4]) + int(matches[5])
    brackets = matches[2]
    print(left, right)

    old = "" if len(matches[0]) < 1 else matches[0]+matches[1]+","
    old += brackets+str(matches[3])+","+str(matches[4])+"],"+str(matches[5])
    new = "0,"+str(right)
  else:
    matches = re.findall("([0-9])+,\\[([0-9]+),([0-9]+)(]{4,}),*(\\[)*([0-9])*", number)
    matches = matches[0]
    print(matches)
  
    left = int(matches[0]) + int(matches[1])
    right = int(matches[2]) + int(matches[5]) if len(matches[5]) > 0 else 0
    brackets = matches[3]
    print(left, right)

    old = matches[0]+",["+matches[1]+","+matches[2]+brackets
    new = str(left)+",0"+brackets[1:]
    if len(matches[5]) > 0:
      old += ","+matches[4]+matches[5]
      new += ","+matches[4]+str(right)
    print(old, new)

  return number.replace(old, new)