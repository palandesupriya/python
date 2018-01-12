def add(iNum1, iNum2, iNum3 = 0, iNum4 = 0, iNum5 = 0):
	return iNum1 + iNum2 + iNum3 + iNum4 + iNum5

def main():
	print("Addition of two numbers:{}".format(add(2,3)))
	print("Addition of three numbers:{}".format(add(2,3,4)))
	print("Addition of four numbers:{}".format(add(2,3,4,5)))
	print("Addition of five numbers:{}".format(add(2,3,4,5,6)))

if __name__ == '__main__':
	main()