'''
WAP to accept file name and display alternate n(or config this) characters.(use seek)
'''

def readalter(szfnm, iNum):
	fp = open(szfnm, "r")
	chFirstAltr = ""
	chSecondAltr = ""
	chFirstAltr = fp.read(iNum)
	while(chFirstAltr != ""):
		print chFirstAltr
		fp.seek(iNum, 1)
		chFirstAltr = fp.read(iNum)

	print("****************************************************")
	fp.seek(iNum, 0)
	chFirstAltr = fp.read(iNum)
	while(chFirstAltr != ""):
		print chFirstAltr
		fp.seek(iNum, 1)
		chFirstAltr = fp.read(iNum)

def main():
	szfnm = input("Enter a file name:")
	#szfnm = "hw.txt"
	iNum = input("Enter characters to skip:")
	readalter(szfnm, iNum)

if __name__ == '__main__':
	main()
