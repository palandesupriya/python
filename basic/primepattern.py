import math
def IsPrime(iNum):
	if (0 == iNum % 2):
		return False
	iTemp = 2
	while (iTemp < math.sqrt(iNum)):
		if (0 == iNum % iTemp):
			return False
		iTemp += 2
	return True
	
def pattern(iNum):
	for iRow in range(1, iNum + 1):
		iStart = (iRow*(iRow + 1))/2
		for iCol in range(1, iRow + 1):
			if (1 == iRow):
				print("2"),
			else:
				while(True):
					if (IsPrime(iStart)):
						print(iStart),
						iStart += 1
						break
					else:
						iStart += 1
		print("")

def main():
	iRow = input("Enter rows:")
	pattern(iRow)
	
if __name__ == '__main__':
	main()
