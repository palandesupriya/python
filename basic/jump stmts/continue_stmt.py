'''

WAP to accpet range from user and display numbers in that range.

'''

def display(iStart, iEnd):
	for iTemp in range(iStart, iEnd + 1):
		if (0 == iTemp%2 or 0 == iTemp%3):
			continue
		print iTemp
		
		
def main():
	iNum1 = input("Enter lower bound:")
	iNum2 = input("Enter upper bound:")
	display(iNum1, iNum2)
	
if __name__ == '__main__':
	main()