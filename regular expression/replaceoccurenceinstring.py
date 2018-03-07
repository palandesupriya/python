'''
WAP to accept string from user, accept replaceto and replaceby string as well and number of occurences
to be replaced in the given string of replaceto by replaceby. do not use any built in replace function.
'''

import re
def replaceex(szStr, iStart, iEnd, szReplaceBy):
	szFirst = szStr[0:iStart]
	szSecond = szStr[iEnd:]
	return (szFirst+szReplaceBy+szSecond)
	
def replaceoccurence(szString, szReplace, szReplaceBy):
	lst = []
	x = re.search(szReplace, szString)
	iStart = 0
	while x != None:
		if szReplace == szString[x.start() + iStart: x.end() + iStart]:
			szString = replaceex(szString, x.start() + iStart, x.end() + iStart, szReplaceBy)
			iStart += (len(szReplace) - len(szReplace))
		iStart += x.end()
		x = re.search(szReplace, szString[iStart:])
	return szString
	
def main():
	szString = input("Enter string:")
	szReplaceTo = input("Enter replace to:")
	szReplaceBy = input("Enter replace by:")
	print("Replacing {} in {} by {} is {}".format(szReplaceTo, szString, szReplaceBy, replaceoccurence(szString, szReplaceTo, szReplaceBy)))
	
if __name__ == '__main__':
	main()
