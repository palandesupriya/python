'''
WAP to accept 2 no from user and check if both of them have same no of '0' and '1' bits.
'''
def CountOneBitsPos(no):
	no = abs(no)
	x = 1 
	count = 0 	
	while x <= no:
		if no & x !=0:
			count += 1
		x = x << 1
	return count
def main():
	n1 = input("Enter a number:")
	n2 = input("Enter another number:")
	bits1 = CountOneBitsPos(n1)
	bits2 = CountOneBitsPos(n2)
	if bits1 == bits2:
		print("Both have same number of zeros and ones")
	elif (n1 > 0 and n2 < 0) and (bits1 == (bits2-1)):
		print("Both have same number of zeros and ones")
	else:
		print("Both do not have same number of zeros and ones")
if __name__ == '__main__':
	main()