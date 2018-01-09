'''
WAP to print:
Number of rows = 5 then output :
*********
**** ****
***   ***
**     **
*       *

'''
def pattern(iNum):
	for iRow in range(iNum+1):
		if 0 == iRow:
			for iCol in range(iNum*2-1):
				print("*"),
			print("")
		else:
			for iCol in range(iNum - iRow):
				print("*"),
				
			for iCol in range(2*iRow - 1):
				print(" "),
			
			for iCol in range(iNum - iRow):
				print("*"),
				
			print("")

def main():
	iRow = input("Enter rows:")
	pattern(iRow)
	
if __name__ == '__main__':
	main()
