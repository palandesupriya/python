'''

WAP to accept a number form user and display its factorial

'''

def factorial(iNum):
	iFact = 1
	for iTemp in range(2, iNum + 1):
		iFact *= iTemp
	return iFact
	
def main():
	iNum = input("Enter number:")
	print("Fatorial is :", factorial(iNum))

if __name__ == '__main__':
	main()