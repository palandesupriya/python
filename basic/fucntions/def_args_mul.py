'''

WAP to demonstrate default arguments. Addition program.

'''
def multiply(iNum1, iNum2, iNum3 = 1, iNum4 = 1, iNum5 = 1):
	return iNum1 * iNum2 * iNum3 * iNum4 * iNum5

def main():
	print("Multiplication of two numbers:{}".format(multiply(2,3)))
	print("Multiplication of three numbers:{}".format(multiply(2,3,4)))
	print("Multiplication of four numbers:{}".format(multiply(2,3,4,5)))
	print("Multiplication of five numbers:{}".format(multiply(2,3,4,5,6)))

if __name__ == '__main__':
	main()