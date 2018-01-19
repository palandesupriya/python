'''

WAP to count number of bits ON in a postive number

'''
def CountOneBits(no):
	x = 1 
	count = 0 
	while x <= no:
		if no & x !=0:
			count += 1
		x = x << 1
	return count
	
def main():
	iNum = input("Enter a number:")
	print("Number of bits On in {} are {}".format(iNum, CountOneBits(iNum)))
	
if __name__ == '__main__':
	main()