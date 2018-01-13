'''

WAP to accept n numbers from user and display their addition.
Note: use variable number of arguments

'''
def add(*iNum):
	iSum = 0
	for iTemp in iNum:
		iSum += iTemp
	return iSum

def main():
	print("Addition of two numbers:{}".format(add(2,3)))
	print("Addition of three numbers:{}".format(add(2,5,5)))
	print("Addition of four numbers:{}".format(add(2,3,4,5)))
	print("Addition of five numbers:{}".format(add(2,3,4,5,6)))

if __name__ == '__main__':
	main()