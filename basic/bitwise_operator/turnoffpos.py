'''
WAP to accept a num and pos from where to turn off bits and no.to turn off number of bits.
Turn off respective bits from the given pos and display result
'''
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
		print("1.Off\n2.ON\n3.Toggle\n4.Power of 2 check\n4.EXIT")
		iChoice = input("Enter choice:")
		if iChoice > 0 & iChoice < 5:
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
		'''elif 4 == iChoice:
			iNum = input("Enter a number:")
			if (pow2(iNum)):
				print("{} is in power of  2".format(iNum))
			else:
				print("{} is not in power of  2".format(iNum))'''
		elif 5 == iChoice:
			break
		else:
			break
	
def main():
	ExecuteChoice()
	
if __name__ == '__main__':
	main()
