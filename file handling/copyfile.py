'''
WAP which copies source file to destination file.
The arguments will come as command line arguments.
copy.py <srcfile> <destfile>
'''

import sys
import argparse
def copycontent(src, dest, n):
	fp1 = open(src, "r")
	fp2 = open(dest, "a")
	if 0 == n:
		lines = fp1.readlines()
		fp2.writelines(lines)
	else:
		line = fp1.readline()
		while n > 0:
			fp2.write(line)
			line = fp1.readline()
			if line == "":
				break
			n -= 1
		fp2.flush()
	fp1.close()
	fp2.close()
	
def main():
	print sys.argv
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--srcfile", type = str, help = "Input/source file")
	parser.add_argument("-d", "--destfile", type = str, help = "destination file")
	parser.add_argument("-n", "--iLine", type = int, help = "Number of lines to read", default = 0)
	args = parser.parse_args()
	copycontent(args.srcfile, args.destfile, args.iLine)
	
if __name__ == '__main__':
	main()
		