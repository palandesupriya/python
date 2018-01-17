def Mul8(iNum):
	bFlag = False
	if iNum & 7 == 0:
		bFlag = True
	return bFlag
	
def main():
	iNum = input("Enter number:")
	if (Mul8(iNum)):
		print("{} is a multiple of 8".format(iNum))
	else:
		print("{} is NOT multiple of 8".format(iNum))
		
if __name__	==	'__main__':
	main()