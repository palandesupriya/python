'''
(1) WAP to accept directory path from user and type of files to be deleted recursively from given directory.
'''
import os.path
def del_callback(arg, dir, files):
	print("Deleting all {} files".format(arg))
	for file in files:
		if file.endswith(arg):
			print(os.path.join(dir, file) + "removed successfully")
			os.remove(os.path.join(dir, file))

def main():
	drnm = input("Enter directory name/path:")
	ext = input("Enter extension of files to del:")
	os.path.walk(drnm, del_callback, ext)
	
if __name__ == '__main__':
	main()