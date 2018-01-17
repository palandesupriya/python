def Mul32(iNum):
	bFlag = False
	if iNum & 15 == 0:
		bFlag = True
	return bFlag
	
def main():
	iNum = input("Enter number:")
	if (Mul32(iNum)):
		print("{} is a multiple of 32".format(iNum))
	else:
		print("{} is NOT multiple of 32".format(iNum))
		
if __name__	==	'__main__':
	main()