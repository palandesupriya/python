'''
implement complex number: add a number to complex number, add two complex numbers
							subtract a number from complex number, subtract two complex numbers
							x + iy 
'''
class Complex:

	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	
	def __del__(self):
		print("Destructor")
		
	def getValues(self):
		return self.x, self.y
		
	def setValues(self, x, y):
		self.x = x
		self.y= y
		
	def add(self, obj1, obj2):
		self.x = obj1.x + obj2.x
		self.y = obj1.y + obj2.y
	
	def subtract(self, obj1, obj2):
		self.x = obj1.x - obj2.x
		self.y = obj1.y - obj2.y
		
	def show(self):
		print("{}+{}i".format(self.x, self.y))
	
def main():
	obj1 = Complex()
	obj2 = Complex()
	objAdd = Complex()
	objSubtract = Complex()
	
	ix1, iy1 = input("Enter x and y for first complex number:")
	obj1.setValues(ix1, iy1)
	
	ix2, iy2 = input("Enter x and y for second complex number:")
	obj2.setValues(ix2, iy2)

	print("Addition of complex numbers:")
	obj1.show()
	obj2.show()
	print("Result:"),
	objAdd.add(obj1, obj2)
	objAdd.show()
	
	print("Substraction of complex numbers:")
	obj1.show()
	obj2.show()
	print("Result:"),
	objSubtract.subtract(obj1, obj2)
	objSubtract.show()
	
if __name__ == '__main__':
	main()