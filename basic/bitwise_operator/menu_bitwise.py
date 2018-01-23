'''
WAP to create a menu for bitwise operations:
1.Turn OFF bits in a number
2.Similarly turn ON bits
3.Toggle bits in a number
4.Check if a number lies in power of 2
5.Check if a number is divisible by its divisor
6.Swap bits of two numbers
7.CRC packets creation and depackatisation
'''

#=========================================================
#+
#SWAP bits starts here

def TurnOFFPos(iNum, iPos, iBits):
	iDummy = (1 << iBits) - 1	# or we can use iDummy = (2 ** iBits) - 1
	iDummy = iDummy << (iPos - iBits)
	iDummy = ~iDummy
	return iNum & iDummy
	
def FetchRangeTurnedON(iPos, iBits):
	iTurnONTotalBits = (2**iBits) - 1
	return iTurnONTotalBits << (iPos - iBits)

def FetchRangeOfBits(iNum, iPos, iBits):
	iRangeON = FetchRangeTurnedON(iPos, iBits)
	return iNum & iRangeON
	
def swapbits(iNum1, iNum2, iPos1, iPos2, iBits):
	iXSpecifcRange = FetchRangeOfBits(iNum1, iPos1, iBits)
	iYSpecificRange = FetchRangeOfBits(iNum2, iPos2, iBits)
	
	iX = TurnOFFPos(iNum1, iPos1, iBits)
	iY = TurnOFFPos(iNum2, iPos2, iBits)
	
	iAnsX = iX | iYSpecificRange
	iAnsY = iY | iXSpecifcRange
	
	print("{} is now {}  and {} is now {}".format(iNum1, iAnsX, iNum2, iAnsY))
#-
#SWAP bits end here
#=========================================================

#=========================================================
#+
#CRC starts here


def FetchRangeON(iBits):
	return 2**iBits - 1
	
def FetchBitsOfNum(iNum, iBits):
	iRange = FetchRangeON(iBits)
	return iRange & iNum
	
def GetPacket(iCRC, iLen, iData, iFlag):
	iPacket = 0
	iPacket |= FetchBitsOfNum(iCRC, 5)
	iPacket <<= 8
	iPacket |= FetchBitsOfNum(iLen, 8)
	iPacket <<= 18
	iPacket |= FetchBitsOfNum(iData, 18)
	iPacket <<= 1
	iPacket |= FetchBitsOfNum(iFlag, 1)

	return iPacket

def Depackatise(iPacket):
	iFlag = FetchBitsOfNum(iPacket, 1)
	
	iPacket >>= 1
	iData = FetchBitsOfNum(iPacket, 18)
	
	iPacket >>= 18
	iLen = FetchBitsOfNum(iPacket, 8)
	
	iPacket >>= 8
	iCRC = FetchBitsOfNum(iPacket, 5)
	
	print("CRC = {}".format(iCRC))
	print("Len = {}".format(iLen))
	print("Data = {}".format(iData))
	print("Flag = {}".format(iFlag))


#-
#CRC ends here
#=========================================================

def Generic2sPowerDivisibiltyTest(iNum, iDiv):
	return (iNum & (iDiv - 1)) == 0

def pow2(iNum):
	return 0 == (iNum & (iNum - 1))
	
def Toggle(iNum, iPos, iBits):
	iDummy = (1 << iBits) - 1	# or we can use iDummy = (2 ** iBits) - 1
	iDummy = iDummy << (iPos - iBits)
	return iNum ^ iDummy
	
def TurnONPos(iNum, iPos, iBits):
	iDummy = (1 << iBits) - 1	# or we can use iDummy = (2 ** iBits) - 1
	iDummy = iDummy << (iPos - iBits)
	return iNum | iDummy
	
def TurnOFFPos(iNum, iPos, iBits):
	iDummy = (1 << iBits) - 1	# or we can use iDummy = (2 ** iBits) - 1
	iDummy = iDummy << (iPos - iBits)
	iDummy = ~iDummy
	return iNum & iDummy
	
def Menu():
	while True:
		print("1.Off\n2.ON\n3.Toggle\n4.Power of 2 check")
		print("5.Check divisibility of number\n6.Swap bits of two numbers\n7.CRC packet\n8.EXIT")
		iChoice = input("Enter choice:")
		if iChoice > 0 & iChoice < 8:
			return iChoice
			
def ExecuteChoice():
	while True:
		iChoice = Menu()
		if 1 == iChoice:
			iNum = input("Enter a number:")
			iPos = input("Enter a position:")
			iBits = input("Enter number of bits:")
			print("{} with turned off bits {} from position {} is {}".format(iNum, iBits, iPos, TurnOFFPos(iNum, iPos, iBits)))
			
		elif 2 == iChoice:
			iNum = input("Enter a number:")
			iPos = input("Enter a position:")
			iBits = input("Enter number of bits:")
			print("{} with turned on bits {} from position {} is {}".format(iNum, iBits, iPos, TurnONPos(iNum, iPos, iBits)))
			
		elif 3 == iChoice:
			iNum = input("Enter a number:")
			iPos = input("Enter a position:")
			iBits = input("Enter number of bits:")
			print("{} with toggled bits {} from position {} is {}".format(iNum, iBits, iPos, Toggle(iNum, iPos, iBits)))
			
		elif 4 == iChoice:
			iNum = input("Enter a number:")
			if (pow2(iNum)):
				print("{} is in power of  2".format(iNum))
			else:
				print("{} is not in power of  2".format(iNum))
				
		elif 5 == iChoice:
			iNum = input("Enter a number:")
			iDiv = input("Enter a divisor:")
			if (Generic2sPowerDivisibiltyTest(iNum, iDiv)):
				print("{} is in power of  {}".format(iNum, iDiv))
			else:
				print("{} is not in power of  {}".format(iNum, iDiv))
				
		elif 6 == iChoice:
			iNum1 = input("Enter a number:")
			iNum2 = input("Enter another number:")
			
			iPos1 = input("Enter position for first number:")
			iPos2 = iPos1
			szChoice = input("Enter same pos for second number(Y/N)?")
			if ("N" == szChoice):
				iPos2 = input("Enter position for second number:")
				
			iBits = input("Enter bits:")
			swapbits(iNum1, iNum2, iPos1, iPos2, iBits)
			
		elif 7 == iChoice:
			iCRC = input("Enter CRC:")
			iLen = input("Enter length:")
			iData = input("Enter data:")
			iFlag = input("Enter Flag:")
			iPacket = GetPacket(iCRC, iLen, iData, iFlag)
			print("Your packet is {}".format(iPacket))
			print("Data to packet was after depackatisation:")
			Depackatise(iPacket)
			
		else:
			break
			
		szChoice = input("\n\nContinue to Menu(Y/N)?")
		if ("N" == szChoice):
			break
	
def main():
	ExecuteChoice()
	
if __name__ == '__main__':
	main()