'''
Reverse file contents.
'''
def revfile(fd):
	line = fd.readline()
	if line == "":
		return
	revfile(fd)
	print line
	
def main():
	fnm = input("Enter file to read:")
	fp = open(fnm, "r")
	print revfile(fp)
	fp.close()
	
if __name__ == '__main__':
	main()
