import threading
import time
def worker():
	time.sleep(3)
	print "worker finished execution"
	
def main():
	tHandle = threading.Thread(target = worker)
	tHandle.start()
	tHandle.join()
	for i in range(1, 6):
		print i
		
if __name__ == '__main__':
	main()
	
'''
OUTPUT without join method:
	1
	2
	3
	4
	5
	worker finished execution
	
OUTPUT with join method:
	worker finished execution
	1
	2
	3
	4
	5
'''
