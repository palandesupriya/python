'''

WAP to accpet number from user and heck if armstrong.
153 = 1^3 + 5^3 + 3^3
'''

def CheckArmstrong(iNum):
	iTemp = iNum
	iCubeSum = 0
	while(iTemp != 0):
		iCubeSum += ((iTemp%10)**3)
		iTemp = iTemp/10
		
	bFlag = False
	if iNum == iCubeSum:
		bFlag = True
	return bFlag
	
def main():
	iNum1 = input("Enter a number:")
	if (CheckArmstrong(iNum1)):
		print("Number is armstrong")
	else:
		print("Number is not armstrong")
	
if __name__ == '__main__':
	main()