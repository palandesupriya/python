'''
Write your own findall that returns list of all matched pattern.
use search and slice repeatedly
Have list of tuple of start and end

Similar inbuilt function is:
>>> x = re.finditer('h', 'hellohieeheybye')
>>> for y in x:
...  print y.start(),y.end()
...
0 1
5 6
9 10
'''
import re
def findallex(pattern, st):
	lst = []
	x = re.search(pattern, st)
	iStart = 0
	while x != None:
		tuple = (x.start() + iStart, x.end() + iStart)
		lst.append(tuple)
		iStart += x.end()
		x = re.search(pattern, st[iStart:])
		#iStart += x.end()
	print lst
	
def main():
	findallex('h', 'hellohieeheybye')
	#findallex('h', 'fgdfgdfg')
	
if __name__ == '__main__':
	main()
	
