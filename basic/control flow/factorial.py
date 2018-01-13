'''

WAP to accept a number form user and display its factorial

'''
#non-recursive function
def factorial(iNum):
	iFact = 1
	iNum = abs(iNum)	#for negative numbers, convert to positive numbers
	for iTemp in range(2, iNum + 1):
		iFact *= iTemp
	return iFact
	
#direct-recursive function
def xfactorial(iNum):
	if (2 > iNum):
		return 1
	return iNum * xfactorial(iNum-1)

def main():
	iNum = input("Enter number:")
	print("Fatorial is :", factorial(iNum))
	print("Fatorial is :", xfactorial(iNum))

if __name__ == '__main__':
	main()
