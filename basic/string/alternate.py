def PrintAlternate(szStr):
	szAlterStr = szStr[0:2] + szStr[len(szStr) - 2:] + szStr[2:len(szStr)-2:2] + szStr[3:len(szStr)-2:2]
	print("Alternater char string {}".format(szAlterStr))
def main():
	szStr = input("Enter a string:")
	PrintAlternate(szStr)
if __name__ == '__main__':
	main()
