'''
Argument Parser based assignment:
	WAP command line based for performing file related operations:
		-operarion copy -s -d
		-operarion compare -s -d
		-operarion append -s -d
'''
import sys
import argparse
def copyex(szsrc, szdest):
	fp1 = open(szsrc, "r")
	fp2 = open(szdest, "w")
	lines = fp1.readlines()
	fp2.writelines(lines)
	fp1.close()
	fp2.close()

def cmpex(szsrc, szdest):
	fp1 = open(szsrc, "r")
	fp2 = open(szdest, "r")
	lines1 = fp1.readlines()
	lines2 = fp2.readlines()
	if lines1 == lines2:
		print("Both files contain same data")
	else:
		print("Both files do not contain same data")
	fp1.close()
	fp2.close()

def appendex(szsrc, szdest):
	fp1 = open(szsrc, "r")
	fp2 = open(szdest, "a")
	lines1 = fp1.readlines()
	fp2.writelines(lines1)
	fp1.close()
	fp2.close()

def main():
	print sys.argv
	parser = argparse.ArgumentParser()
	parser.add_argument("-op", "--operation", type = str, help = "File operation to perform")
	parser.add_argument("-s", "--srcfile", type = str, help = "Source or input file")
	parser.add_argument("-d", "--destfile", type = str, help = "Destination or output file")
	args = parser.parse_args()
	if "copy" in args.operation:
		copyex(args.srcfile, args.destfile)
	elif "compare" in args.operation:
		cmpex(args.srcfile, args.destfile)
	elif "append" in args.operation:
		appendex(args.srcfile, args.destfile)
	else:
		print("Invalid Command Specified!!")
		
if __name__ == '__main__':
	main()