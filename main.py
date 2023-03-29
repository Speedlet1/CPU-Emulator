import instructions
import time
i = open("instructionRAM.txt", "r+")
instructionread = i.read()
instructionarray = instructionread.split(" ")
accumulator=0x0
address=0
addresscell=1
PC=0
address=instructionarray[addresscell]
while addresscell<=len(instructionarray):
  addressadd1=instructionarray[addresscell+1]
  address=instructionarray[addresscell]
  time.sleep(0.20)
  C=True
  #beginning of instruction search logic
  if int(instructionarray[PC],16)==0:
    accumulator=instructions.lda(address)
  elif int(instructionarray[PC],16)==1:
    instructions.sta(address,accumulator)
  elif int(instructionarray[PC],16)==2:
    accumulator=instructions.add(address, accumulator)
  elif int(instructionarray[PC],16)==3:
    accumulator=instructions.sub(address, accumulator)
  elif int(instructionarray[PC],16)==4:
    accumulator=instructions.mul(address,accumulator)
  elif int(instructionarray[PC],16)==5:
    accumulator=hex(instructions.div(address,accumulator))
  elif int(instructionarray[PC],16)==6:
    instructions.out(accumulator)
  elif int(instructionarray[PC],16)==7:
    accumulator=instructions.inp()
  elif int(instructionarray[PC],16)==8:
    PC=instructions.bra(address)
    addresscell=PC+1
    C=False
  elif int(instructionarray[PC],16)==9:
    PC=instructions.brp(address, accumulator)
    addresscell=PC+1
    C=False
  elif int(instructionarray[PC],16)==10:
    PC=instructions.brz(address, accumulator)
    addresscell=PC+1
    C=False
  elif int(instructionarray[PC],16)==11:
    PC=instructions.bre(address, accumulator, addressadd1)
    addresscell=PC
    C=False
  elif int(instructionarray[PC],16)==12:
    break
  #end of instruction search logic
  if int(accumulator,16)>=256:
    print("Error: Accumulator value too large: Maximum of 8 bit numbers")
    break
  if C==True:
    addresscell+=2
    PC=addresscell-1