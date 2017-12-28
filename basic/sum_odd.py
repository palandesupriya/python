'''
WAP to find sum of all odd numbers
in the given range.
'''
def IsOdd(iNum):
	if (0 != iNum & 1):
		return True
	return False
def main():
	iStart = input("Enter start num:")
	iEnd = input("Enter end num:")
	if (iStart < iEnd):
		iSum = 0
		for iTemp in range(iStart, iEnd + 1):
			if (IsOdd(iTemp)):
				iSum += iTemp
		print ("Sum of all odd numbers: {}".format(iSum))
if __name__ == '__main__':
	main()
