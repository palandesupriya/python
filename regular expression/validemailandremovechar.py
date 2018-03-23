'''
1)WAP to validate E-mail ID using regular expressions
2)WAP to accept an alphanumeric string from user and remove all characters other than digits
	using regular expressions
'''
import re
def verifyemail(szEmail):
	
	#regExpr = re.search("[a-zA-Z0-9]+\@{1}[a-zA-Z]+\.{1}[a-zA-Z]+", szEmail)
	regExpr = "([\w\.]+)@([\w\.]+)\.(\w+)"
	if None == regExpr:
		return False
	if len(szEmail) == regExpr.end():
		return True
	return False

def rmCharFromString(szStr):
	x = re.findall("[a-zA-Z]+", szStr)
	i = 0
	while i < len(x):
		szStr = re.sub(x[i], "", szStr, 1)
		i += 1
	print("Removed all characters from string:{}".format(szStr))

def main():
	szEmailID = input("Enter e-mail ID:")
	bRet = verifyemail(szEmailID)
	if True == bRet:
		print("Correct Email-ID")
	else:
		print("Incorrect Email-ID")
		
	rmCharFromString(szEmailID)
if __name__ == '__main__':
	main()
