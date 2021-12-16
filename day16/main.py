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

def getPacketLength(packetString):
  index = 6
  lastGroup = False
  while lastGroup == False:
    currentGroup = packetString[index:index+5]
    index += 5
    if currentGroup[0] == "0":
      lastGroup = True 
  print("packetLength", index)
  return index

def isOperatorPacket(packetString):
   type = int(packetString[3:6], 2)
   print("type", type)
   return type != 4

def calculatePacketVersion(packetString):
  print("packetString", packetString)
  version = getVersion(packetString)
  if isOperatorPacket(packetString):
    lengthType = getLengthType(packetString)
    if lengthType == 0:
      packetLength = int(packetString[7:22], 2)
      index = 22
    else:
      subPacketCount = int(packetString[7:18], 2)
      index = 18
    version += calculatePacketVersion(packetString[index:])
  return version

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

  binaryString = "".join([letterToBinary[x] for x in input])
  print("binaryString", binaryString)
  version = calculatePacketVersion(binaryString)
  return version


