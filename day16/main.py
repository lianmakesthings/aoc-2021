import sys
def readFile(filepath):
  f = open(filepath, "r")
  content = f.readlines()
  return content[0]

def getVersion(string):
  version = int(string[:3], 2)
  print("version", version)
  return version

def getLengthType(packetString):
  lengthType = int(packetString[6])
  print("lengthType", lengthType)
  return lengthType

def getType(string):
  type = int(string[3:6], 2)
  print("type", type)
  return type

def isNumberPacket(string):
  return getType(string) == 4

def getPacketLength(packetString):
  if isNumberPacket(packetString):
    index = 6
    lastGroup = False
    while lastGroup == False:
      currentGroup = packetString[index:index+5]
      index += 5
      if currentGroup[0] == "0":
        lastGroup = True 
    print("packetLength", index)
    return index
  elif getLengthType(packetString) == 0:
    length = int(packetString[7:22], 2)
    print("length type 0", length)
    return length
  else:
    print(packetString[7:18])
    packetCount = int(packetString[7:18], 2)
    index = 18
    print("packetCount", packetCount)
    for x in range(packetCount):
      length = getPacketLength(packetString[index:])
      index += length
    print("length type 1", index)
    return index

def calculatePacketVersion(packetString):
  print("packetString", packetString)
  if len(packetString) < 11:
    return 0
  version = getVersion(packetString)

  if isNumberPacket(packetString):
    packetLength = getPacketLength(packetString)
    version += calculatePacketVersion(packetString[packetLength:])
  else:
    lengthType = getLengthType(packetString)
    index = 0
    if lengthType == 0:
      packetLength = int(packetString[7:22], 2)
      index = 22
      version += calculatePacketVersion(packetString[index:index+packetLength])
      version += calculatePacketVersion(packetString[index+packetLength:])
    else:
      index = 18
      version += calculatePacketVersion(packetString[index:])

  return version

def letterToBinary(letter):
  map = {
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
  return map[letter]

def first(filepath):
  input = readFile(filepath)
  binaryString = "".join([letterToBinary(x) for x in input])
  print("binaryString", binaryString)
  version = calculatePacketVersion(binaryString)
  return version

def isSumPacket(string):
  return getType(string) == 0

def isProductPacket(string):
  return getType(string) == 1

def isMinimumPacket(string):
  return getType(string) == 2

def isMaximumPacket(string):
  return getType(string) == 3

def isGreaterPacket(string):
  return getType(string) == 5

def isLessPacket(string):
  return getType(string) == 6

def isEqualPacket(string):
  return getType(string) == 7

def calculatePacketValue(string):
  print("string", string)
  if len(string) > 4:
    if isSumPacket(string):
      sum = 0
      if getLengthType(string) == 1:
        packetCount = int(string[7:18], 2)
        print("packet count", packetCount)
        sum = 0
        index = 18
        for x in range(packetCount):
          length = getPacketLength(string[index:])
          sum += calculatePacketValue(string[index:index+length])
          index += length
      else:
        sum = 0
        index = 22
        lastIndex = index + getPacketLength(string)
        while index < lastIndex:
          print("here", index, lastIndex, string[:index])
          length = getPacketLength(string[index:])
          print(length)
          sum += calculatePacketValue(string[index:index+length])
          index += length
      print("sum", sum)
      return sum
    elif isProductPacket(string):
      product = 1
      if getLengthType(string) == 1:
        packetCount = int(string[7:18], 2)
        print("packet count", packetCount)
        index = 18
        for x in range(packetCount):
          length = getPacketLength(string[index:])
          product *= calculatePacketValue(string[index:index+length])
          index += length
      else:
        index = 22
        length = getPacketLength(string)
        lastIndex = index+length
        while index < lastIndex:
          length = getPacketLength(string[index:])
          product *= calculatePacketValue(string[index:index+length])
          index += length
      print("product", product)
      return product
    elif isMinimumPacket(string):
      numbers = []
      if getLengthType(string) == 1:
        packetCount = int(string[7:18], 2)
        index = 18
        for x in range(packetCount):
          length = getPacketLength(string[index:])
          value = int(calculatePacketValue(string[index:index+length]))
          numbers.append(value)
          index += length
      else:
        product = 1
        index = 22
        length = getPacketLength(string)
        lastIndex = index+length
        while index < lastIndex:
          value = int(calculatePacketValue(string[index:index+length]))
          numbers.append(value)
          index += getPacketLength(string[index:])
      return min(numbers)
    elif isMaximumPacket(string):
      numbers = []
      if getLengthType(string) == 1:
        packetCount = int(string[7:18], 2)
        index = 18
        for x in range(packetCount):
          length = getPacketLength(string[index:])
          value = int(calculatePacketValue(string[index:index+length]))
          numbers.append(value)
          index += length
      else:
        product = 1
        index = 22
        length = getPacketLength(string)
        lastIndex = index+length
        while index < lastIndex:
          value = int(calculatePacketValue(string[index:index+length]))
          numbers.append(value)
          index += getPacketLength(string[index:])
      return max(numbers)
    elif isGreaterPacket(string):
      index = 0
      length = getPacketLength(string)
      firstValue = 0
      secondValue = 0
      if getLengthType(string) == 0:
        index = 22
        length = getPacketLength(string[index:])
        for x in range(2):
          if x == 0:
            firstValue = calculatePacketValue(string[index:index+length])
          else:
            secondValue = calculatePacketValue(string[index:index+length])
          index += length
      else:
        index = 18
        for x in range(2):
          length = getPacketLength(string[index:])
          if x == 0:
            firstValue = calculatePacketValue(string[index:index+length])
          else:
            secondValue = calculatePacketValue(string[index:index+length])
          index += length
      return 1 if firstValue > secondValue else 0
    elif isLessPacket(string):
      index = 0
      length = getPacketLength(string)
      firstValue = 0
      secondValue = 0
      if getLengthType(string) == 0:
        index = 22
        length = getPacketLength(string[index:])
        for x in range(2):
          if x == 0:
            firstValue = calculatePacketValue(string[index:index+length])
          else:
            secondValue = calculatePacketValue(string[index:index+length])
          index += length
      else:
        index = 18
        for x in range(2):
          length = getPacketLength(string[index:])
          if x == 0:
            firstValue = calculatePacketValue(string[index:index+length])
          else:
            secondValue = calculatePacketValue(string[index:index+length])
          index += length
      return 1 if firstValue < secondValue else 0
    elif isEqualPacket(string):
      index = 0
      firstValue = 0
      secondValue = 0
      if getLengthType(string) == 0:
        index = 22
        length = getPacketLength(string)
        for x in range(2):
          if x == 0:
            firstValue = calculatePacketValue(string[index:index+length])
            print("first value", firstValue)
            index += getPacketLength(string[index:])
          else:
            print("second value", string[index:])
            secondValue = calculatePacketValue(string[index:])
          print(index)
          
      else:
        index = 18
        for x in range(2):
          length = getPacketLength(string[index:])
          if x == 0:
            firstValue = calculatePacketValue(string[index:index+length])
          else:
            secondValue = calculatePacketValue(string[index:])
          index += length
      return 1 if firstValue == secondValue else 0
    elif isNumberPacket(string):
      index = 6
      lastGroup = False
      number = ""
      while lastGroup == False:
        currentGroup = string[index:index+5]
        print("current group", currentGroup)
        index += 5
        if currentGroup[0] == "0":
          lastGroup = True
        number += currentGroup[1:]
      print("number", int(number, 2))
      return int(number, 2)
      

def second(filepath):
  input = readFile(filepath)
  binaryString = "".join([letterToBinary(x) for x in input])

  return calculatePacketValue(binaryString)

print(second("input.txt"))