def fact(iNum):
	ifact =  1
	while iNum > 0:
		ifact = ifact * iNum
		iNum -= 1
	return ifact
def specialnum(iNum):
	isum = 0
	while iNum > 0:
		isum = isum + fact(iNum%10)
		iNum = iNum/10
	return isum
def main():
	inum = input("Enter a number:")
	if inum == specialnum(inum):
		print("{} is a special number.".format(inum))
	else:
		print("{} is not a special number.".format(inum))

if __name__ == '__main__':
	main()