def GetReverse(iNum):
	iTemp = 0
	while(0 != iNum):
		iTemp = (iNum % 10) + (iTemp * 10)
		iNum = iNum / 10
	return iTemp
	
def IsPalindrome(iNum):
	if (GetReverse(iNum) == iNum):
		return True
	return False
	
def main():
	iNum = input("Enter number:")
	if (IsPalindrome(iNum)):
		print("{} is palindrome.".format(iNum))
	else:
		print("{} is not palindrome.".format(iNum))
		
if __name__ == '__main__':
	main()
