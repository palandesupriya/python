'''
WAP to traverse given directory and cnt number of python files in it.
Recursively traverse all directories.
'''
import os.path
py_cnt = 0
other_cnt = 0
def main():
	os.path.walk("E:\\pyprograms", cnt_callback, "Directory traverse count")
	print("Total python files:{}".format(py_cnt))
	print("Total other files:{}".format(other_cnt))
	
def cnt_callback(arg, directry, files):
	global py_cnt
	global other_cnt
	for file in files:
		if file.endswith(".py"):
			py_cnt += 1
		else:
			other_cnt += 1

if __name__ == '__main__':
	main()
