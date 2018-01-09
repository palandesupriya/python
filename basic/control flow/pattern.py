def pattern1(iNumRows):
	for iTempRows in range(0, iNumRows):
		for iTempCol in range(0, iTempRows + 1):
			print("*"),
		print("")
		
		
def pattern2(iNumRows):
	for iTempRows in range(0, iNumRows):
		for iTempCol in range(0, iNumRows - iTempRows):
			print("*"),
		print("")
		
def pattern3(iNumRows):
	for iTempRows in range(0, iNumRows):
		iChar = 97
		for iTempCol in range(0, iTempRows + 1):
			print(chr(iChar)),
			iChar = iChar + 1
		print("")
		
def main():
	iRows = input("Enter rows:")
	pattern1(iRows)
	print("")
	pattern2(iRows)
	print("")
	pattern3(iRows)
if __name__ == '__main__':
	main()
