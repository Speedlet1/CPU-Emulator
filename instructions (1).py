d = open("dataRAM.txt", "r+")
dataread = d.read()
dataarray = dataread.split(" ")
def lda(address):
  accumulator=hex(int(dataarray[int(address,16)],16))
  return accumulator

def sta(address,accumulator):
  dataarray[int(address,16)]=str(accumulator)
  dataarray1=" ".join(dataarray)
  d = open("dataRAM.txt", "w")
  d.write(dataarray1)
  
def add(address, accumulator):
  accumulator=int(accumulator,16)+int(dataarray[int(address,16)],16)
  return hex(accumulator)
  
def sub(address, accumulator):
  if int(accumulator,16)>=int(dataarray[int(address,16)]):
    accumulator=hex(int(accumulator,16)-int(dataarray[int(address,16)]))
  else:
    print("Negative error - please subtract a different value")
  return accumulator
  
def mul(address, accumulator):
  accumulator=hex(int(accumulator,16)*int(dataarray[int(address,16)],16))
  return accumulator
  
def div(address, accumulator):
  accumulator=int(accumulator,16)//int(dataarray[int(address,16)])
  if accumulator!=int(accumulator):
    print("Does not return integer, please try with a different combination of numbers")
    error=True
    return error
  else:
    return accumulator
    
def out(accumulator):
  print(accumulator)
  print(int(accumulator,16))
  print("\n")
  
def inp():
  register=int(input("Please enter the value you would like to be stored in the ACC in denary"))
  return hex(register)
  
def bra(address):
  instructioncell=(int(address,16))
  return instructioncell
  
def brn(address, accumulator):
  if int(accumulator,16)==0:
    instructioncell=int(address,16)
  return instructioncell
  
def brp(address, accumulator):
  if int(accumulator,16)>0:
    instructioncell=int(address,16)
  return instructioncell

def bre(address, accumulator, PC):
  if int(accumulator,16)==int(dataarray[int(address,16)],16):
    PC=int(PC,16)
  return int(PC,16)