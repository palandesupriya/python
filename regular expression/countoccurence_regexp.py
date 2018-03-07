'''
WAP to accept pattern and string from user and count occurences of pattern in string
using search method
'''
import re
def countalloccurence(pattern, st):
	lst = []
	x = re.search(pattern, st)
	iStart = 0
	iCnt = 0
	while x != None:
		if pattern == st[x.start() + iStart: x.end() + iStart]:
			iCnt += 1
		iStart += x.end()
		x = re.search(pattern, st[iStart:])
	return iCnt
	
def main():
	szString = input("Enter string:")
	szPattern = input("Enter pattern:")
	print("Occurence of {} in {} are {}".format(szPattern, szString,countalloccurence(szPattern, szString)))
	
if __name__ == '__main__':
	main()
