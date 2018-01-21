'''

WAP to accept following values from user CRC, length, data and flag
where CRC is 5-bits, length is 8-bits and data is 18 bits and flag is 1-bit
Combine and create a packate.
Again depackatise.

'''

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
	
def main():
	iCRC = input("Enter CRC:")
	iLen = input("Enter length:")
	iData = input("Enter data:")
	iFlag = input("Enter Flag:")
	iPacket = GetPacket(iCRC, iLen, iData, iFlag)
	print("Your packet is {}".format(iPacket))
	print("Data to packet was after depackatisation:")
	Depackatise(iPacket)
	
if __name__ == '__main__':
	main()