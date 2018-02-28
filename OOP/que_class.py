'''
implement queue using class
'''
class Queue:
	def __init__(self, size = 5):
		self.size = size
		self.lst = [] 
		
	def add(self, value):
		if False == self.isFull():
			self.lst.append(value)
		else:
			print("STACK IS FULL!!!!")
		
	def remove(self):
		if False == self.isEmpty():
			print("Element is:{}".format(self.lst.pop(0)))
		else:
			print("QUEUE IS EMPTY!!!!")
			
	def isFull(self):
		if self.size == len(self.lst):
			return True
		return False
		
	def isEmpty(self):
		if 0 == len(self.lst):
			return True
		return False
		
def main():
	queobj = Queue()
	print("1.Add element to queue")
	print("2.Remove element to queue")
	print("3.Check empty queue")
	print("4.Check full queue")
	print("5.EXIT")
	ch = input("Enter choice:")
	while 5 != ch:
		if 1 == ch:
			val = input("Enter element to push:")
			queobj.add(val)
		elif 2 == ch:
			queobj.remove()
		elif 3 == ch:
			print("Queue empty : {}".format(queobj.isEmpty()))
		elif 4 == ch:
			print("Queue full : {}".format(queobj.isFull()))
		elif 5 == ch:
			break
		ch = input("Enter choice:")
	
if __name__ == '__main__':
	main()