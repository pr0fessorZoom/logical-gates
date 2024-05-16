def andGate (a, b):
  if a == 1 and b == 1:
    return 1
  else:
    return 0
  
def orGate (a, b):
  return a or b
  
def xorGate (a, b):
  if a == b:
    return 0
  else:
    return 1
  
def nandGate (a, b):
  # return not andGate(a, b) // Esta deberia ser la respuesta si quiero true o false
  if a == 1 and b == 1:
    return 0
  else:
    return 1
  
def norGate (a, b):
  # return not orGate(a, b) # Esta deberia ser la respuesta si quiero true o false
  if a == 0 and b == 0:
    return 1
  else:
    return 0
  
def xnorGate (a, b):
  if a == b:
    return 1
  else:
    return 0

def tests():
  print("andGate test: " + str(andGate(1, 1)))
  print("andGate test: " + str(andGate(0, 1)))
  print("andGate test: " + str(andGate(1, 0)))
  print("andGate test:" + str(andGate(0, 0)))
  print("orGate test: " + str(orGate(1, 1)))
  print("orGate test: " + str(orGate(0, 1)))
  print("orGate test: " + str(orGate(1, 0)))
  print("orGate test: " + str(orGate(0, 0)))
  print("xorGate test: " + str(xorGate(1, 1)))
  print("xorGate test: " + str(xorGate(0, 1)))
  print("xorGate test: " + str(xorGate(1, 0)))
  print("xorGate test: " + str(xorGate(0, 0)))
  print("nandGate test: " + str(nandGate(1, 1)))
  print("nandGate test: " + str(nandGate(0, 1)))
  print("nandGate test: " + str(nandGate(1, 0)))
  print("nandGate test: " + str(nandGate(0, 0)))
  print("norGate test: " + str(norGate(1, 1)))
  print("norGate test: " + str(norGate(0, 1)))
  print("norGate test: " + str(norGate(1, 0)))
  print("norGate test: " + str(norGate(0, 0)))
  print("xnorGate test: " + str(xnorGate(1, 1)))
  print("xnorGate test: " + str(xnorGate(0, 1)))
  print("xnorGate test: " + str(xnorGate(1, 0)))
  print("xnorGate test: " + str(xnorGate(0, 0)))
  
if '__main__' == __name__:
  tests()