'''
WAP to accept two directory names from user and check if both of them contains same files.
'''
import sys
import os.path
import argparse
dir_files_first = []
dir_files_sec = []
def main():
	print sys.argv
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--dirffile", type = str, help = "Directory to compare")
	parser.add_argument("-c", "--dirsfile", type = str, help = "Directory to comapre with")
	args = parser.parse_args()
	os.path.walk(args.dirffile, dir1_callback, "directory 1")
	os.path.walk(args.dirsfile, dir2_callback, "directory 2")
	
	if dir_files_first == dir_files_sec:
		print("Both directories contain same file.")
	else:
		print("Both directories do not contain same files.")
def dir1_callback(arg, directry, files):
	print arg
	for file in files:
		dir_files_first.append(file)

def dir2_callback(arg, directry, files):
	print arg
	for file in files:
		dir_files_sec.append(file)

if __name__ == '__main__':
	main()
		