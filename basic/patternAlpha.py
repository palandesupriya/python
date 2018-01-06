def pattern1(iNumRow):
	iNum = 97
	for iRow in range(0, iNumRow):
		iIndex = iRow
		for iCol in range(1, iNumRow - iRow):
			print(" "),
		for iCol in range(0, (2*iRow) + 1):
			print(chr(iNum+iIndex)),
			if (iCol >= (iRow)):
				iIndex = iIndex + 1
			else:
				iIndex = iIndex - 1
		print("")

def main():
	iRow = input("Enter rows:")
	pattern1(iRow)
	
if __name__ == '__main__':
	main()
