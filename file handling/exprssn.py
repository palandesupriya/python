'''
WAP which compute value of following expression
	a+aa+aaa+aaaa+..............
	2+22
	3+33+333
	4+44+444+4444
'''
def getexprss(iNum):
	temp = iNum
	szExpression = str(iNum)
	sum = iNum
	for i in range(1,iNum):
		szExpression += "+"
		tempNum = iNum*(10**i)+temp
		sum += tempNum
		szExpression += str(tempNum)
		temp = tempNum
	print("{}={}".format(szExpression, sum))
def main():
	while (1):
		iNum = input("Enter digit:")
		if (iNum >= 1 and iNum <= 9):
			break
		else:
			print("Enter valid digit.")
	getexprss(iNum)
if __name__ == '__main__':
	main()
