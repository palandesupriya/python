'''
implement complex number: add a number to complex number, add two complex numbers
							subtract a number from complex number, subtract two complex numbers
							x + iy

__Add__ and __contains__ are operator overloaded functions.							
'''
class Complex:

	def __init__(self, ix = 0, iy = 0):
		self.ix = ix
		self.iy = iy
	
	def __del__(self):
		print("Destructor")
		
	def getValues(self):
		return self.ix, self.iy
		
	def setValues(self, ix, iy):
		self.ix = ix
		self.iy= iy
		
	def __add__(self, iValue):
		obj = Complex()	
		if isinstance(iValue, Complex): 	#OR we could use if (Complex == type(iValue))
			obj.ix = self.ix + iValue.ix
			obj.iy = self.iy + iValue.iy
		elif isinstance(iValue, int):
			obj.ix = self.ix + iValue.ix
			obj.iy = self.iy
			
	def subtract(self, obj1, obj2):
		self.ix = obj1.ix - obj2.ix
		self.iy = obj1.iy - obj2.iy
		
	def __repr__(self):
		return str(self.ix + "+i" + self.iy)
	
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
	print("Result:"),
	objAdd = obj1+ obj2
	print objAdd
	
	print("Substraction of complex numbers:")
	print("Result:"),
	objSubtract = obj1 - obj2
	print objSubtract
	
if __name__ == '__main__':
	main()