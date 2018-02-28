class Stack:
	def __init__(self, size = 5):
		self.size = size
		self.lst = [] 
		
	def push(self, value):
		if False == self.isFull():
			self.lst.append(value)
		else:
			print("STACK IS FULL!!!!")
		
	def pop(self):
		if False == self.isEmpty():
			print("Element is:{}".format(self.lst.pop()))
		else:
			print("STACK IS EMPTY!!!!")
			
	def isFull(self):
		if self.size == len(self.lst):
			return True
		return False
		
	def isEmpty(self):
		if 0 == len(self.lst):
			return True
		return False
		
def main():
	stkobj = Stack()
	print("1.Add element to stack")
	print("2.Remove element to stack")
	print("3.Check empty stack")
	print("4.Check full stack")
	print("5.EXIT")
	ch = input("Enter choice:")
	while 5 != ch:
		if 1 == ch:
			val = input("Enter element to push:")
			stkobj.push(val)
		elif 2 == ch:
			stkobj.pop()
		elif 3 == ch:
			print("Stack empty : {}".format(stkobj.isEmpty()))
		elif 4 == ch:
			print("Stack full : {}".format(stkobj.isFull()))
		elif 5 == ch:
			break
		ch = input("Enter choice:")
	
if __name__ == '__main__':
	main()