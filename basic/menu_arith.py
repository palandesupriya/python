def add(iNum1, iNum2):
	return (iNum1 + iNum2)
def subtract(iNum1, iNum2):
	return (iNum1 - iNum2)
def multiply(iNum1, iNum2):
	return (iNum1 * iNum2)
def divide(iNum1, iNum2):
	if (0 == iNum2):
		return 0;
	return (iNum1 / iNum2)

def main():
	while(True):
		iChoice = input("Enter choice(+,-,*,/):")
		if (iChoice not in ['+','-','*','/']):
			print("Invalid choice.Exit.")
			break
		iNum1, iNum2 = input("Enter two numbers seperated by comma:")
		if ('+' == iChoice):
			iRes = add(iNum1, iNum2)
			print("Result of {} is {}".format(iChoice, iRes))
		elif ('-' == iChoice):
			iRes = subtract(iNum1, iNum2)
			print("Result of {} is {}".format(iChoice, iRes))
		elif ('*' == iChoice):
			iRes = multiply(iNum1, iNum2)
			print("Result of {} is {}".format(iChoice, iRes))
		elif ('/' == iChoice):
			iRes = division(iNum1, iNum2)
			print("Result of {} is {}".format(iChoice, iRes))

if __name__ == '__main__':
	main()
