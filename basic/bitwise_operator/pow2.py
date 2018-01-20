'''

WAP to check if a number is in power of 2.

'''
def pow2(iNum):
	return 0 == (iNum & (iNum - 1))
	
def mulpow2(iNum):
	iNum = abs(iNum)
	x = 1
	cnt = 0
	bFlag = True
	while x <= iNum:
		if iNum & x != 0:
			#print(x)
			cnt += 1
		if 2 == cnt:
			bFlag = False
			break
		x = x << 1
		
	return bFlag
	
def main():
	iNum = input("Enter a number:")
	'''if (mulpow2(iNum)):
		print("{} is in power of  2".format(iNum))
	else:
		print("{} is not in power of  2".format(iNum))'''
		
	if (pow2(iNum)):
		print("{} is in power of  2".format(iNum))
	else:
		print("{} is not in power of  2".format(iNum))
		
if __name__ == '__main__':
	main()