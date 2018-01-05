'''
WAP to find occurences of string in other string.
'''
def Occur(szStrSrc, szStrSub):
	iLenSub = len(szStrSub)
	iCnt = 0
	for iTemp in range(0, len(szStrSrc) - iLenSub):
		szTempStr = szStrSrc[iTemp : iTemp + iLenSub]
		print(szTempStr)
		if (szTempStr == szStrSub):
			iCnt += 1
	return iCnt
def main():
	szStr = input("Enter string:")
	szSubStr = input("Enter sub-string:")
	iCnt = Occur(szStr, szSubStr)
	print("Occurences of {} in {} is {}".format(szSubStr, szStr, iCnt))
	
if __name__ == '__main__':
	main()