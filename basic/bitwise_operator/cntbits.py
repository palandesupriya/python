'''

WAP to count number of bits ON in a postive number and negative number

'''
def CountOneBitsNeg(no):
	x = 1 
	count = 0 
	while x <= max(2**32 - 1, 2**64 - 1):
		if no & x !=0:
			count += 1
		x = x << 1
	return count
	
def CountOneBitsPos(no):
	x = 1 
	count = 0 	
	while x <= no:
		if no & x !=0:
			count += 1
		x = x << 1
	return count
	
def main():
	iNum = input("Enter a number:")
	if (iNum < 0):
		print("Number of bits On in {} are {}".format(iNum, CountOneBitsNeg(iNum)))
	else:
		print("Number of bits On in {} are {}".format(iNum, CountOneBitsPos(iNum)))
	
if __name__ == '__main__':
	main()
