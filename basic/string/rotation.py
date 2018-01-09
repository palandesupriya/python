'''
WAP to check if a string is right roation of given string.
input:	India
		ndiaI
output: True

input:	India
		dianI
output: False
'''
def IsRightRotation(szStr1, szStr2):
	if (len(szStr1) != len(szStr2)):
		return False
	szTemp = szStr1 + szStr1
	if (-1 == szTemp.find(szStr2)):
		return False
	return True
	
def main():
	szStr1 = input("Enter a string:")
	szStr2 = input("Enter string to check for rotation:")
	if (IsRightRotation(szStr1, szStr2)):
		print("{} is right rotation of {}", szStr1, szStr2)
	else:
		print("{} is not right rotation of {}", szStr1, szStr2)
	
if __name__ == '__main__':
		main()
