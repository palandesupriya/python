import re
def PrintLineStartWithChar(inFile,skipChar):
	pattern = "^" + skipChar + ".*"
	print pattern
	x = re.compile(pattern, re.MULTILINE | re.IGNORECASE)
	fd = open(inFile)
	buf = fd.read()
	res = x.findall(buf)
	print res
	
def main():
	inFile = input("Enter name of file: ")
	skipChar = input("Enter character to skip: ")
	PrintLineStartWithChar(inFile,skipChar)
  
if __name__=="__main__":
	main()
