'''
1. WAP to accept a name of a file from user and print count of lines present in that file based on following filters
	- if filter comes as a empty string - count total lines using readline()
	- if filter="^Hello" the line count should be of lines which starts with "Hello"
	- if filter="Hello$" - count ends with Hello
	- if neither above then check for contains "Hello" and count lines.
'''
def findsubstr(szStr, szFilter):
	iCnt = 0
	szFilter = szFilter.lower()
	if "^hello" == szFilter:
		szTemp = szStr[0: len("hello"):]
		szTemp = szTemp.lower()
		if szTemp == "hello":
			iCnt = 1
	elif "hello$" == szFilter:
		szTemp = szStr[len(szStr) - len("hello") - 1: len(szStr) - 1:]
		szTemp = szTemp.lower()
		if szTemp == "hello":
			iCnt = 1
	elif "hello" == szFilter:
		szStr = szStr.lower()
		if 1 <= szStr.count("hello"):
			iCnt = 1
	else:
		iCnt = 1
		
	return iCnt

def findfile(filename, szFilter = ""):
	iCnt = 0
	fp = open(filename, "r")
	line = fp.readline()
	while line != "":
		iCnt = iCnt + findsubstr(line, szFilter)
		line = fp.readline()
		
	print("Total Lines :{}".format(iCnt))
		
def main():
	inFilename = "Hello.txt"
	#inFilename = input("Enter filename:")
	szFilter = input("Enter filter(^Hello, Hello$, Hello):")
	findfile(inFilename, szFilter)
	
if __name__ == '__main__':
	main()