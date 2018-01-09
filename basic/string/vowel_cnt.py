'''
WAP to count total vowels and consonants
present in a given string.
'''
def IsVowel(szChar):
	if (szChar in ['a','e','i', 'o','u']):
		return True
	return False
def main():
	szStr = input("Enter a string:")
	icVowel = 0
	icConsonant = 0
	for szChar in szStr:
		if (IsVowel(szChar)):
			icVowel += 1
		else:
			icConsonant += 1
	print("Total vowels {1} and total consonants {0}".format(icConsonant, icVowel))
if __name__ == '__main__':
	main()
