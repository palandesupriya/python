'''
WAP to accept name of file and display longest and smallest line from the same.
'''
def findlargestandsmallest(szFilenm):
	fp = open(szFilenm, "r")
	line = fp.readline()
	max = len(line)
	min = len(line)
	szMax = line
	szMin = line
	lines = fp.readlines()
	for line in lines:
		ilen = len(line)
		if ilen >= max:
			max = ilen
			szMax = line
		if ilen <= min:
			min = ilen
			szMin = line
	print("Shortest line is:{}".format(szMin))
	print("Longest line is:{}".format(szMax))

def main():
	infilenm = "hello.txt"
	findlargestandsmallest(infilenm)
	
	
if __name__ == '__main__':
	main()