iNum1=input("Enter number")
iNum2=input("Enter number")
iNum3=input("Enter number")
if (iNum1 > iNum2 and iNum1 > iNum3):
	print("Greatest number is:", iNum1)
elif (iNum2 > iNum3):
	print("Greatest number is:", iNum2)
else:
	print("Greatest number is:", iNum3)
	
if (iNum1 < iNum2 and iNum1 < iNum3):
	print("Smallest number is:", iNum1)
elif (iNum2 < iNum3):
	print("Smallest number is:", iNum2)
else:
	print("Smallest number is:", iNum3)
