'''

WAP to accpet two numbers from user , accpet pos and number of bits to be swapped from the given tow numbers

'''
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
	
def main():
	iNum1 = input("Enter a number:")
	iNum2 = input("Enter another number:")
	
	iPos1 = input("Enter position for first number:")
	iPos2 = iPos1
	szChoice = input("Enter same pos for second number(Y/N)?")
	if ("N" == szChoice):
		iPos2 = input("Enter position for second number:")
		
	iBits = input("Enter bits:")
	swapbits(iNum1, iNum2, iPos1, iPos2, iBits)
	
if __name__ == '__main__':
	main()