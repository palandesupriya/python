import threading
import time
def worker(szName):
	time.sleep(3)
	print("worker finished execution : {}".format(szName))
	
def main():
	szName = "Supriya Palande"
	tHandle = threading.Thread(target = worker, args = (szName,)) # , is important, otherwise error thrown
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
	worker finished execution Supriya Palande
	
OUTPUT with join method:
	worker finished execution Supriya Palande
	1
	2
	3
	4
	5
'''
