'''

WAP to check if a number is multiple of 2/4/8/16/32/64/...

3 bits -- 8
4 bits -  16
5 bits -  32
6 bits -  64
7 bits -  128

'''

def Generic2sPowerDivisibiltyTest(iNum, iDiv):
	return (iNum & (iDiv - 1)) == 0
	
def main():
	iNum = input("Enter a number:")
	iDiv = input("Enter a divisor:")
	if (Generic2sPowerDivisibiltyTest(iNum, iDiv)):
		print("{} is in power of  {}".format(iNum, iDiv))
	else:
		print("{} is not in power of  {}".format(iNum, iDiv))
		
if __name__ == '__main__':
	main()
