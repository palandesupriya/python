'''
WAP to accept file name and display alternate n(or config this) characters.(use seek)
'''
def readalter(szfnm, iNum):
	fp = open(szfnm, "r")
	ch = fp.read(1)
	szAlter = ""
	while(ch != ""):
		szAlter += ch
		fp.seek(iNum, 1)
		ch = fp.read(1)
	print szAlter
def main():
	#szfnm = input("Enter a file name:")
	szfnm = "hw.txt"
	iNum = input("Enter characters to skip:")
	readalter(szfnm, iNum)
if __name__ == '__main__':
	main()