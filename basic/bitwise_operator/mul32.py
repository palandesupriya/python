def Mul32(iNum):
	return iNum & 15
	
def main():
	iNum = input("Enter number:")
	if (0 == Mul32(iNum)):
		print("{} is a multiple of 32".format(iNum))
	else:
		print("{} is NOT multiple of 32".format(iNum))
		
if __name__	==	'__main__':
	main()
