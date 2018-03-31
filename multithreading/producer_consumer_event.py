'''

Producer consumer problem using Events.

'''
from threading import Thread
from threading import Event
import time
data = []
size = 0
producer_event = Event()
consumer_event = Event()

def read():
	global data
	global size
	global producer_event
	global consumer_event
	print("Inside consumer...")
	while True:
		producer_event.wait()
		print "\nConsumed", data[0]
		del data[0]
		size -= 1
		consumer_event.set()
		producer_event.clear()
		
def write():
	global data
	global size
	global producer_event
	while True:
		x = input("Enter data:")
		data.append(x)
		size += 1
		producer_event.set()
		if  10 == size:
			consumer_event.wait()
			consumer_event.clear()
	
	
def main():
	producer_thread = Thread(target = write)
	consumer_thread = Thread(target = read)
	producer_thread.start()
	consumer_thread.start()
	
if __name__ == '__main__':
	main()
