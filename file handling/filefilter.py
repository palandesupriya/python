'''
1. WAP to accept a name of a file from user and print count of lines present in that file based on following filters
	- if filter comes as a empty string - count total lines using readline()
	- if filter="^substr" the line count should be of lines which starts with "substr"
	- if filter="substr$" - count ends with substr
	- if neither above then check for contains "substr" and count lines.
'''
def findsubstr(szStr, szFilter):
	iCnt = 0
	szFilter = szFilter.lower()
	if szFilter.startswith("^"):
		szTemp = szStr[0: len(szFilter)-1:]
		szTemp = szTemp.lower()
		if szTemp == szFilter[1:]:
			iCnt = 1
	elif szFilter.endswith("$"):
		szTemp = szStr[len(szStr) - (len(szFilter) -1 )- 1: len(szStr) - 1:]
		szTemp = szTemp.lower()
		if szTemp == szFilter[0: (len(szFilter) - 1)]:
			iCnt = 1
	elif szFilter in szStr:
		szStr = szStr.lower()
		if 1 <= szStr.count(szFilter):
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
