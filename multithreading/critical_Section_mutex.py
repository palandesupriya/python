'''
Critical situation using mutex as lock:
*****************************************************************
PRoblem 1: global data is not synchronised among all threads
from threading import Thread
import time
data = 0
lock = Lock()
def getData():
	global data
	data += 1
	time.sleep(0.1)
	return data
	
def ProcessJob():
	print getData()
	
def main():
	threads = []
	for i in range(10):
		thread = Thread(target = ProcessJob)
		threads.append(thread)
		thread.start()
		
if __name__ == '__main__':
	main()

*****************************************************************
Problem 2: Race condition still occurs here since data is global

from threading import Thread
import time
from threading import Lock
data = 0
lock = Lock()
def getData():
	global data
	lock.acquire()
	data += 1
	time.sleep(0.1)
	lock.release
	return data
	
def ProcessJob():
	print getData()
	
def main():
	threads = []
	for i in range(10):
		thread = Thread(target = ProcessJob)
		threads.append(thread)
		thread.start()
		
if __name__ == '__main__':
	main()
'''
#Hence use local variable which will ensure each thread has its own copy of
#data on its stack frame
from threading import Thread
import time
from threading import Lock
data = 0
lock = Lock()
def getData():
	global data
	lock.acquire()
	data += 1
	x = data
	time.sleep(0.1)
	lock.release()
	return x
	
def ProcessJob():
	print getData()
	
def main():
	threads = []
	for i in range(10):
		thread = Thread(target = ProcessJob)
		threads.append(thread)
		thread.start()
		
if __name__ == '__main__':
	main()
