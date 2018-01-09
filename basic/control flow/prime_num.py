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

def main():
	iNum = input("Enter range for fetching prime numbers:")
	for iTemp in range(2, iNum + 1):
		if (IsPrime(iTemp)):
			print(iTemp)

if __name__ == '__main__':
	main()
