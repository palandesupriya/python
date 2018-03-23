'''
Search words that either start with digit or start with underscore.
'''

import re
def PrintLineStartWithDigitOrUnderscore(inFile):
	x = re.compile(r"\b\d\w+|_\w+", re.MULTILINE)
	fd = open(inFile)
	buf = fd.read()
	res = x.findall(buf)
	print res
	
def main():
	inFile = input("Enter name of file: ")
	PrintLineStartWithDigitOrUnderscore(inFile)
  
if __name__=="__main__":
	main()
