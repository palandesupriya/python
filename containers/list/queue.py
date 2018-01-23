'''

WAP to implement queue using list.

'''
def Enqueue(lst, value):
	if IsFull(lst):
		print("Queue is full!! No more elements can be added.")
	else:
		# if list == type(lst):
			# lst.extend(value)
		# else:
			lst.append(value)
		
def Dequeue(lst):
	if IsEmpty(lst):
		print("Queue is empty!! No elements to fetch.")
	else:
		print("Element from Queue removed is:{}".format(lst.pop(0)))
		
def IsFull(lst):
	return 5 == len(lst)
	
def IsEmpty(lst):
	return 0 == len(lst)
	
def main():
	lst = []
	while True:
		print("\nChoice:\n1.ADD\n2.REMOVE\n3.Check FULL\n4.Check EMPTY\n5.PRINT ALL\n6.EXIT")
		iChoice = input("Enter choice:")
		if 1 == iChoice:
			iNum = input("Enter value to add:")
			Enqueue(lst, iNum)
			
		elif 2 == iChoice:
			Dequeue(lst)
			
		elif 3 == iChoice:
			if (IsFull(lst)):
				print("Queue is FULL!!")
			else:
				print("Queue is not FULL yet!!")
				
		elif 4 == iChoice:
			if (IsEmpty(lst)):
				print("Queue is EMPTY!!")
			else:
				print("Queue is not EMPTY yet!!")
				
		elif 5 == iChoice:
			print lst
			
		else:
			break
			
if __name__ == '__main__':
	main()