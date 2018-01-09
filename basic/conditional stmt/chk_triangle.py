def main():
	iSide1=input("Enter a number")
	iSide2=input("Enter another number")
	iSide3=input("Enter one more number")
	iFlag = 0;
	if (iSide1 + iSide2 > iSide3):
		iFlag = iFlag + 1
	if (iSide1 + iSide3 > iSide2):
		iFlag = iFlag + 1
	if (iSide2 + iSide3 > iSide1):
		iFlag = iFlag + 1
		
	if (3 == iFlag):
		print("Numbers form a triangle")
	else:
		print("Numbers do not form a triangle")
		
if __name__ == '__main__':
	main()
	
