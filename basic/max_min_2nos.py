def main():
	iNumFirst=input("Enter a number")
	iNumSec=input("Enter another number")
	if (iNumFirst > iNumSec):
		print("Max number is:", iNumFirst)
		print("Min number is:", iNumSec)
	elif (iNumFirst < iNumSec):
		print("Max number is:", iNumSec)
		print("Min number is:", iNumFirst)
	else:
		print("Both are equal")
		
if __name__ == '__main__':
	main()