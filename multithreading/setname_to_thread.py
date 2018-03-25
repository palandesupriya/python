import threading
import time
def worker(szName):
	time.sleep(3)
	print("worker finished execution : {}".format(szName))
	print("Explicitely set name to thread as : {}".format(threading.currentThread().getName()))
	
def main():
	szName = "Supriya Palande"
	tHandle = threading.Thread(target = worker, args = (szName,), name = "Interesting") # , is important, otherwise error thrown
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
	Explicitely set name to thread as : Interesting
	
OUTPUT with join method:
	worker finished execution Supriya Palande
	Explicitely set name to thread as : Interesting
	1
	2
	3
	4
	5
'''
