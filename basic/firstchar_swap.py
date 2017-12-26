'''
WAP to accept two strings from user and swap first two char
from both the string.
For eg: If two strings are "Supriya" and "Bingo"
		then output should be "Bipriya" and "Sungo".
	
String Slicing using:
	string_name[start_index_inclusive : end_index_exclusive : step_value]
		where all three are conditional.
'''
def StrJoin(szStr1, szStr2):
	szTemp1 = szStr2[0:2] + szStr1[2:]
	szTemp2 = szStr1[0:2] + szStr2[2:]
	print("Strings are {0} {1} ".format(szTemp1, szTemp2))
def main():
	szStr1 = input("Enter a string:")
	szStr2 = input("Enter another string:")
	StrJoin(szStr1, szStr2)
if __name__ == '__main__':
	main()
