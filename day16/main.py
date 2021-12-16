import sys
def readFile(filepath):
  f = open(filepath, "r")
  content = f.readlines()
  return content[0]

def getVersion(string):
  return int(string[:3], 2)

def packetEndIndex(string):
  type = int(string[3:6], 2)
  index = 0
  if type == 4:
    lastGroup = False
    while lastGroup == False:
      currentGroup = string[index:index+5]
      print(index, currentGroup)
      index += 5
      if currentGroup[0] == "0":
        lastGroup = True
  return index

def first(filepath):
  input = readFile(filepath)
  letterToBinary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
  }

  binary = "".join([letterToBinary[x] for x in input])
  version = getVersion(binary)
  type = int(binary[3:6], 2)
  print(binary, version, type)
  if type == 4:
    # lastGroup = False
    # index = 6
    # value = ""
    # while lastGroup == False:
    #   currentGroup = binary[index:index+5]
    #   value += currentGroup[1:]
    #   print(value, currentGroup)
    #   index += 5
    #   if currentGroup[0] == "0":
    #     lastGroup = True
    print("literal")
  else:
    lengthType = int(binary[6])
    if lengthType == 0:
      length = int(binary[7:22], 2)
      print(lengthType, length)
      index = 22
      while index < len(binary):
        version += getVersion(binary[index:])
        index += packetEndIndex(binary[index:])
        print(index, len(binary))

    else:
      subPacketCount = int(binary[7:18], 2)
      print(lengthType, subPacketCount)
  print(version)


